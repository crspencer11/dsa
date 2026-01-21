from typing import Set
from enum import Enum, auto
import re

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
    
    @staticmethod
    def to_snake_case(value: str) -> str:
        if not value:
            return ""
        
        value = re.sub(r"[\-\.\s]+", " ", value)
        value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
        value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
        value = re.sub(r"([a-z]+)([a-z][a-z]+)", r"\1_\2", value)

        return value.strip().lower().replace(" ", "_")

    def grant_permission(self, role: RoleType, permission: str) -> None:
        if role not in self.ROLE_PERMISSIONS:
            raise ValueError(f"Role {role} does not exist")

        if permission in self.ROLE_PERMISSIONS[role]:
            raise ValueError(f"Permission '{permission}' already granted to {role.name}")

        # grant permission to the role && recalc effective permissions
        permission = self.to_snake_case(permission)
        self.ROLE_PERMISSIONS[role].add(permission)
        self.effective_permissions = self._get_all_permissions(self.user_role)
        print(f"Permission {permission} added to role {role.name}")

    def has_access(self, permission: str) -> bool:
        return permission in self.effective_permissions

admin_session = RBAC(RoleType.ADMIN)
print(f"Admin can read? {admin_session.has_access('read_file')}") # True via inheritance
admin_session.grant_permission(RoleType.ADMIN, 'deletegroup')