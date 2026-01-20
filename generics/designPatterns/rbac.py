from typing import Set
from enum import Enum, auto

class RoleType(Enum):
    ADMIN = auto()
    ELEVATED = auto()
    BASIC = auto()

class RBAC:
    # define parents acting as a graph traversing downwards
    HIERARCHY = {
        RoleType.ADMIN: [RoleType.ELEVATED],
        RoleType.ELEVATED: [RoleType.BASIC],
        RoleType.BASIC: []
    }

    # role-specific permissions
    ROLE_PERMISSIONS = {
        RoleType.ADMIN: {"delete_user", "edit_settings"},
        RoleType.ELEVATED: {"create_file", "edit_file"},
        RoleType.BASIC: {"read_file", "get_users"}
    }

    def __init__(self, role: RoleType):
        self.user_role = role
        # pre-calculate for O(1) checking
        self.effective_permissions = self._get_all_permissions(role)

    def _get_all_permissions(self, role: RoleType) -> Set[str]:
        """
        A recursive approach to gather permissions. 
        This handles any changes to the HIERARCHY map automatically.
        """
        # start with permissions directly assigned to this role
        permissions = set(self.ROLE_PERMISSIONS.get(role, []))
        for child_role in self.HIERARCHY.get(role, []):
            permissions.update(self._get_all_permissions(child_role))
            
        return permissions
    
    def grant_access(self, permission: str) -> None:
        if permission in self.effective_permissions:
            return ValueError("Permission already granted!")
        
        self.effective_permissions.add(permission)
        return None

    def has_access(self, permission: str) -> bool:
        return permission in self.effective_permissions

admin_session = RBAC(RoleType.ADMIN)
print(f"Admin can read? {admin_session.has_access('read_file')}") # True via inheritance