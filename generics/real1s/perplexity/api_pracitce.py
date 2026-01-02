# Perplexity API - Forward-Deployed Engineer Practice Problems
# These problems reflect the role: API integration, debugging, customer-facing solutions

"""
PROBLEM 1: API Client with Robust Error Handling (15 min)
Build a Python client for the Perplexity API that handles common failure scenarios.

Requirements:
- Implement retry logic with exponential backoff for rate limits (429) and server errors (5xx)
- Handle timeout errors gracefully
- Support both streaming and non-streaming responses
- Validate API responses and handle malformed JSON
- Log errors appropriately for debugging

Example usage:
    client = PerplexityClient(api_key="your_key")
    response = client.chat_completion(
        messages=[{"role": "user", "content": "What is quantum computing?"}],
        model="sonar-pro",
        stream=False
    )
"""

import os
import time
import json
import requests
from typing import Dict, List, Optional, Generator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PerplexityAPIError(Exception):
    """Base exception for Perplexity API errors"""
    pass


class RateLimitError(PerplexityAPIError):
    """Raised when rate limit is exceeded"""
    pass


class PerplexityClient:
    def __init__(self, api_key: str, base_url: str = "https://api.perplexity.ai"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
    
    def _make_request_with_retry(
        self, 
        endpoint: str, 
        payload: Dict,
        max_retries: int = 3,
        timeout: int = 30
    ) -> requests.Response:
        """Make API request with exponential backoff retry logic"""
        
        url = f"{self.base_url}{endpoint}"
        
        for attempt in range(max_retries):
            try:
                response = self.session.post(url, json=payload, timeout=timeout)
                
                # Handle rate limiting
                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 2 ** attempt))
                    logger.warning(f"Rate limited. Retrying after {retry_after}s")
                    time.sleep(retry_after)
                    continue
                
                # Handle server errors with exponential backoff
                if response.status_code >= 500:
                    if attempt < max_retries - 1:
                        wait_time = 2 ** attempt
                        logger.warning(f"Server error {response.status_code}. Retrying in {wait_time}s")
                        time.sleep(wait_time)
                        continue
                    else:
                        response.raise_for_status()
                
                # Handle client errors (no retry)
                if 400 <= response.status_code < 500:
                    logger.error(f"Client error: {response.status_code} - {response.text}")
                    response.raise_for_status()
                
                return response
                
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    logger.warning(f"Request timeout. Attempt {attempt + 1}/{max_retries}")
                    continue
                raise PerplexityAPIError("Request timed out after multiple retries")
            
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {e}")
                raise PerplexityAPIError(f"Request failed: {e}")
        
        raise PerplexityAPIError("Max retries exceeded")
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "sonar-pro",
        stream: bool = False,
        max_tokens: Optional[int] = None
    ) -> Dict:
        """Send chat completion request"""
        
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream
        }
        
        if max_tokens:
            payload["max_tokens"] = max_tokens
        
        response = self._make_request_with_retry("/chat/completions", payload)
        
        try:
            return response.json()
        except json.JSONDecodeError:
            logger.error(f"Failed to decode JSON response: {response.text}")
            raise PerplexityAPIError("Invalid JSON response from API")


"""
PROBLEM 2: Customer Integration Debugger (20 min)
A customer's API integration is failing intermittently. Write a diagnostic tool
that helps identify the root cause.

Given: Customer is calling the API 100 times per minute and seeing ~10% failures
Task: Build a diagnostic script that:
1. Simulates their usage pattern
2. Captures detailed error information
3. Identifies patterns in failures (rate limits, timeouts, etc.)
4. Provides actionable recommendations

This tests: debugging skills, understanding of API limitations, customer empathy
"""

class APIDebugger:
    def __init__(self, client: PerplexityClient):
        self.client = client
        self.results = {
            "total_requests": 0,
            "successful": 0,
            "rate_limited": 0,
            "timeouts": 0,
            "server_errors": 0,
            "client_errors": 0,
            "other_errors": 0,
            "response_times": []
        }
    
    def simulate_customer_usage(self, requests_per_minute: int, duration_minutes: int):
        """Simulate customer usage pattern and collect diagnostics"""
        
        total_requests = requests_per_minute * duration_minutes
        delay = 60.0 / requests_per_minute
        
        logger.info(f"Starting simulation: {requests_per_minute} req/min for {duration_minutes} min")
        
        for i in range(total_requests):
            start = time.time()
            
            try:
                # Simulate customer query
                response = self.client.chat_completion(
                    messages=[{"role": "user", "content": f"Test query {i}"}],
                    model="sonar-pro"
                )
                
                elapsed = time.time() - start
                self.results["successful"] += 1
                self.results["response_times"].append(elapsed)
                
            except RateLimitError:
                self.results["rate_limited"] += 1
                logger.warning(f"Request {i}: Rate limited")
                
            except requests.exceptions.Timeout:
                self.results["timeouts"] += 1
                logger.warning(f"Request {i}: Timeout")
                
            except requests.exceptions.HTTPError as e:
                if 500 <= e.response.status_code < 600:
                    self.results["server_errors"] += 1
                elif 400 <= e.response.status_code < 500:
                    self.results["client_errors"] += 1
                logger.warning(f"Request {i}: HTTP {e.response.status_code}")
                
            except Exception as e:
                self.results["other_errors"] += 1
                logger.error(f"Request {i}: {type(e).__name__}: {e}")
            
            self.results["total_requests"] += 1
            time.sleep(delay)
    
    def generate_report(self) -> str:
        """Generate diagnostic report with recommendations"""
        
        total = self.results["total_requests"]
        if total == 0:
            return "No requests made"
        
        success_rate = (self.results["successful"] / total) * 100
        avg_response_time = sum(self.results["response_times"]) / len(self.results["response_times"]) if self.results["response_times"] else 0
        
        report = f"""
=== API Integration Diagnostic Report ===

Summary:
  Total Requests: {total}
  Successful: {self.results["successful"]} ({success_rate:.1f}%)
  Failed: {total - self.results["successful"]} ({100 - success_rate:.1f}%)

Error Breakdown:
  Rate Limited (429): {self.results["rate_limited"]}
  Timeouts: {self.results["timeouts"]}
  Server Errors (5xx): {self.results["server_errors"]}
  Client Errors (4xx): {self.results["client_errors"]}
  Other Errors: {self.results["other_errors"]}

Performance:
  Avg Response Time: {avg_response_time:.2f}s

Recommendations:
"""
        
        # Generate actionable recommendations
        if self.results["rate_limited"] > 0:
            report += "  ⚠ Rate limiting detected. Implement exponential backoff or reduce request rate.\n"
        
        if self.results["timeouts"] > total * 0.05:
            report += "  ⚠ High timeout rate. Consider increasing timeout or investigating network latency.\n"
        
        if self.results["server_errors"] > 0:
            report += "  ⚠ Server errors detected. Implement retry logic with exponential backoff.\n"
        
        if avg_response_time > 5:
            report += "  ⚠ Slow response times. Consider using streaming or async requests.\n"
        
        return report


"""
PROBLEM 3: Search Result Aggregator (15 min)
Build a tool that makes multiple search queries in parallel and aggregates results
efficiently.

Requirements:
- Accept a list of related queries
- Execute them concurrently (without hitting rate limits)
- Deduplicate results by URL
- Rank by relevance score
- Return top N unique results

This tests: async/concurrent programming, data processing, performance optimization
"""

import asyncio
import aiohttp
from typing import List, Dict, Set
from collections import defaultdict


async def fetch_search_results(
    session: aiohttp.ClientSession,
    api_key: str,
    query: str,
    semaphore: asyncio.Semaphore
) -> List[Dict]:
    """Fetch search results for a single query with rate limiting"""
    
    async with semaphore:  # Limit concurrent requests
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar-pro",
            "messages": [{"role": "user", "content": query}],
            "return_citations": True  # Get source URLs
        }
        
        try:
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("citations", [])
                else:
                    logger.error(f"Query '{query}' failed: {response.status}")
                    return []
        except Exception as e:
            logger.error(f"Error fetching '{query}': {e}")
            return []


async def aggregate_search_results(
    api_key: str,
    queries: List[str],
    max_concurrent: int = 5,
    top_n: int = 10
) -> List[Dict]:
    """
    Execute multiple queries concurrently and aggregate results
    
    Args:
        api_key: Perplexity API key
        queries: List of search queries
        max_concurrent: Max concurrent requests (to avoid rate limits)
        top_n: Number of top results to return
    
    Returns:
        List of deduplicated, ranked results
    """
    
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async with aiohttp.ClientSession() as session:
        # Execute all queries concurrently
        tasks = [
            fetch_search_results(session, api_key, q, semaphore) 
            for q in queries
        ]
        
        all_results = await asyncio.gather(*tasks)
    
    # Aggregate and deduplicate by URL
    url_scores = defaultdict(list)
    url_metadata = {}
    
    for results in all_results:
        for result in results:
            url = result.get("url")
            if url:
                score = result.get("relevance_score", 0)
                url_scores[url].append(score)
                if url not in url_metadata:
                    url_metadata[url] = result
    
    # Calculate average relevance score for each unique URL
    ranked_results = []
    for url, scores in url_scores.items():
        avg_score = sum(scores) / len(scores)
        result = url_metadata[url].copy()
        result["aggregated_score"] = avg_score
        result["appearance_count"] = len(scores)
        ranked_results.append(result)
    
    # Sort by score and appearance count
    ranked_results.sort(
        key=lambda x: (x["aggregated_score"], x["appearance_count"]),
        reverse=True
    )
    
    return ranked_results[:top_n]


"""
PROBLEM 4: Streaming Response Handler (10 min)
Implement a streaming response handler that processes data as it arrives
and handles connection interruptions gracefully.

Requirements:
- Process streaming API responses chunk by chunk
- Handle incomplete chunks (mid-word/mid-sentence)
- Detect and recover from connection drops
- Yield complete sentences as they arrive

This tests: streaming protocols, edge case handling, real-time data processing
"""

def stream_chat_with_recovery(
    client: PerplexityClient,
    messages: List[Dict[str, str]],
    model: str = "sonar-pro"
) -> Generator[str, None, None]:
    """
    Stream chat responses with automatic recovery from interruptions
    
    Yields complete sentences as they arrive
    """
    
    url = f"{client.base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": messages,
        "stream": True
    }
    
    buffer = ""
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            with client.session.post(url, json=payload, stream=True, timeout=60) as response:
                response.raise_for_status()
                
                for line in response.iter_lines():
                    if not line:
                        continue
                    
                    # Parse SSE format: "data: {...}"
                    if line.startswith(b"data: "):
                        data_str = line[6:].decode('utf-8')
                        
                        if data_str == "[DONE]":
                            if buffer:
                                yield buffer
                            return
                        
                        try:
                            data = json.loads(data_str)
                            delta = data.get("choices", [{}])[0].get("delta", {})
                            content = delta.get("content", "")
                            
                            if content:
                                buffer += content
                                
                                # Yield complete sentences
                                while any(p in buffer for p in ['. ', '! ', '? ', '\n']):
                                    for punct in ['. ', '! ', '? ', '\n']:
                                        if punct in buffer:
                                            idx = buffer.index(punct) + len(punct)
                                            yield buffer[:idx]
                                            buffer = buffer[idx:]
                                            break
                        
                        except json.JSONDecodeError:
                            logger.warning(f"Failed to parse chunk: {data_str[:50]}")
                            continue
                
                # Yield any remaining content
                if buffer:
                    yield buffer
                return
                
        except (requests.exceptions.ChunkedEncodingError, 
                requests.exceptions.ConnectionError) as e:
            logger.warning(f"Connection interrupted (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            else:
                raise PerplexityAPIError("Streaming failed after retries")


"""
USAGE EXAMPLES AND TESTING
"""

if __name__ == "__main__":
    # Example 1: Basic client with retry logic
    # client = PerplexityClient(api_key=os.getenv("PERPLEXITY_API_KEY"))
    # response = client.chat_completion(
    #     messages=[{"role": "user", "content": "Explain quantum computing"}],
    #     model="sonar-pro"
    # )
    # print(response)
    
    # Example 2: Debug customer integration
    # debugger = APIDebugger(client)
    # debugger.simulate_customer_usage(requests_per_minute=100, duration_minutes=1)
    # print(debugger.generate_report())
    
    # Example 3: Aggregate search results
    # queries = [
    #     "latest AI research 2025",
    #     "machine learning breakthroughs",
    #     "artificial intelligence papers"
    # ]
    # results = asyncio.run(aggregate_search_results(
    #     api_key=os.getenv("PERPLEXITY_API_KEY"),
    #     queries=queries,
    #     top_n=10
    # ))
    # for r in results:
    #     print(f"{r['aggregated_score']:.2f} - {r['url']}")
    
    # Example 4: Stream with recovery
    # for chunk in stream_chat_with_recovery(client, [
    #     {"role": "user", "content": "Write a long story about space exploration"}
    # ]):
    #     print(chunk, end="", flush=True)
    
    print("Practice problems loaded. Uncomment examples to test.")