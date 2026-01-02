"""
PROBLEM 1: Basic API Client with Retry (20-25 min)
Write a function that calls the Perplexity API and retries on rate limits.

Requirements:
- Make a POST request to /chat/completions
- If you get a 429 (rate limit), wait and retry (max 3 times)
- Return the response or raise an error
"""

import requests
import time

def call_perplexity_api(api_key, prompt, max_retries=3):
    """
    Call Perplexity API with retry logic for rate limits
    
    Args:
        api_key: API key string
        prompt: User question string
        max_retries: Max retry attempts
    
    Returns:
        dict: API response
    """
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    for attempt in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)
        
        # Success
        if response.status_code == 200:
            return response.json()
        
        # Rate limited - retry with backoff
        if response.status_code == 429:
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            print(f"Rate limited, waiting {wait_time}s...")
            time.sleep(wait_time)
            continue
        
        # Other error - don't retry
        response.raise_for_status()
    
    raise Exception("Max retries exceeded")


# Follow-up questions:
# - What if the server returns a 500 error? (Add retry for 5xx too)
# - What if the request times out? (Add timeout parameter)
# - How would you make this work for 1000 queries? (Discuss async/batching)


"""
PROBLEM 2: Parse and Filter Search Results (15-20 min)
Testing data manipulation - Given API responses with citations, extract unique URLs and rank by relevance.

Example input:
[
    {"url": "https://example.com/a", "score": 0.9, "title": "Article A"},
    {"url": "https://example.com/b", "score": 0.7, "title": "Article B"},
    {"url": "https://example.com/a", "score": 0.8, "title": "Article A"},  # duplicate
]

Task: Return top 5 unique URLs, sorted by average score
"""

def rank_search_results(results, top_n=5):
    """
    Deduplicate results by URL and rank by average score
    
    Args:
        results: List of dicts with 'url', 'score', 'title'
        top_n: Number of top results to return
    
    Returns:
        List of dicts with unique URLs, sorted by avg score
    """
    # Group by URL and collect scores
    url_data = {}
    
    for result in results:
        url = result['url']
        if url not in url_data:
            url_data[url] = {
                'url': url,
                'title': result['title'],
                'scores': []
            }
        url_data[url]['scores'].append(result['score'])
    
    # Calculate average scores
    ranked = []
    for url, data in url_data.items():
        avg_score = sum(data['scores']) / len(data['scores'])
        ranked.append({
            'url': url,
            'title': data['title'],
            'avg_score': avg_score,
            'count': len(data['scores'])
        })
    
    # Sort by score and return top N
    ranked.sort(key=lambda x: x['avg_score'], reverse=True)
    return ranked[:top_n]


# Test it
test_results = [
    {"url": "https://example.com/a", "score": 0.9, "title": "Article A"},
    {"url": "https://example.com/b", "score": 0.7, "title": "Article B"},
    {"url": "https://example.com/a", "score": 0.8, "title": "Article A"},
    {"url": "https://example.com/c", "score": 0.95, "title": "Article C"},
]

print(rank_search_results(test_results, top_n=3))
# Expected: Article C (0.95), Article A (0.85), Article B (0.7)


"""
PROBLEM 3: Batch API Calls Without Rate Limits (20 min)
Tests understanding of rate limiting and practical solutions

You need to call the API 100 times but can only make 10 requests per second.
Implement a solution that respects the rate limit.
"""

def batch_api_calls(api_key, prompts, rate_limit=10):
    """
    Make multiple API calls while respecting rate limits
    
    Args:
        api_key: API key
        prompts: List of prompt strings
        rate_limit: Max requests per second
    
    Returns:
        List of responses
    """
    results = []
    delay = 1.0 / rate_limit  # Time between requests
    
    for i, prompt in enumerate(prompts):
        try:
            response = call_perplexity_api(api_key, prompt)
            results.append({"success": True, "data": response})
        except Exception as e:
            results.append({"success": False, "error": str(e)})
        
        # Wait between requests (except on last one)
        if i < len(prompts) - 1:
            time.sleep(delay)
    
    return results


# Follow-up: How would you make this faster?
# Answer: Use async/await with aiohttp to send concurrent requests
# (but still need to throttle to avoid rate limits)

"""
Async version they might ask about:
"""
import asyncio
import aiohttp

async def batch_api_calls_async(api_key, prompts, concurrent_limit=10):
    """
    Make API calls concurrently with a limit on simultaneous requests
    """
    semaphore = asyncio.Semaphore(concurrent_limit)
    
    async def call_api(session, prompt):
        async with semaphore:  # Limit concurrent requests
            url = "https://api.perplexity.ai/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "sonar-pro",
                "messages": [{"role": "user", "content": prompt}]
            }
            
            try:
                async with session.post(url, json=payload, headers=headers) as resp:
                    return await resp.json()
            except Exception as e:
                return {"error": str(e)}
    
    async with aiohttp.ClientSession() as session:
        tasks = [call_api(session, p) for p in prompts]
        return await asyncio.gather(*tasks)


"""
PROBLEM 4: Debug This Code (10-15 min)
Most practical - they show you broken code and ask you to fix it

A customer is reporting errors. What's wrong with this code?
"""

def broken_api_call(api_key, prompt):
    """This code has several bugs - find and fix them"""
    url = "https://api.perplexity.ai/chat/completions"
    
    response = requests.post(url, json={
        "model": "sonar-pro",
        "messages": prompt
    })
    
    data = response.json()
    
    return data['choices'][0]['message']['content']


# Fixed version:
def fixed_api_call(api_key, prompt):
    """Fixed version with proper error handling"""
    url = "https://api.perplexity.ai/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": prompt}]  # Correct format
    }
    
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    
    # Check for errors
    if response.status_code != 200:
        raise Exception(f"API error {response.status_code}: {response.text}")
    
    data = response.json()
    
    # Safely access nested data
    if 'choices' in data and len(data['choices']) > 0:
        return data['choices'][0].get('message', {}).get('content', '')
    
    return None
