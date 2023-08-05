from .lib import lib

from ctypes import c_void_p, c_char_p, c_int, c_uint, c_bool

# auth
BYND_AUTH_TYPE_NONE = 0
BYND_AUTH_TYPE_SINGLE = 1
BYND_AUTH_TYPE_MANAGEMENT = 2

bynd_auth_type_to_string = lib.bynd_auth_type_to_string
bynd_auth_type_to_string.argtypes = [c_int]
bynd_auth_type_to_string.restype = c_char_p

bynd_auth_delete = lib.bynd_auth_delete
bynd_auth_delete.argtypes = [c_void_p]

bynd_auth_get_type = lib.bynd_auth_get_type
bynd_auth_get_type.argtypes = [c_void_p]
bynd_auth_get_type.restype = c_int

bynd_auth_get_competition = lib.bynd_auth_get_competition
bynd_auth_get_competition.argtypes = [c_void_p]
bynd_auth_get_competition.restype = c_char_p

bynd_auth_get_action = lib.bynd_auth_get_action
bynd_auth_get_action.argtypes = [c_void_p]
bynd_auth_get_action.restype = c_char_p

bynd_auth_get_permissions = lib.bynd_auth_get_permissions
bynd_auth_get_permissions.argtypes = [c_void_p]
bynd_auth_get_permissions.restype = c_void_p

bynd_auth_permissions_iter_start = lib.bynd_auth_permissions_iter_start
bynd_auth_permissions_iter_start.argtypes = [c_void_p]
bynd_auth_permissions_iter_start.restype = c_bool

bynd_auth_permissions_iter_get_next = lib.bynd_auth_permissions_iter_get_next
bynd_auth_permissions_iter_get_next.argtypes = [c_void_p]
bynd_auth_permissions_iter_get_next.restype = c_void_p

bynd_auth_create = lib.bynd_auth_create
bynd_auth_create.argtypes = [c_int]
bynd_auth_create.restype = c_void_p

bynd_single_authentication = lib.bynd_single_authentication
bynd_single_authentication.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p]
bynd_single_authentication.restype = c_uint

bynd_management_authentication = lib.bynd_management_authentication
bynd_management_authentication.argtypes = [c_void_p, c_void_p]
bynd_management_authentication.restype = c_uint

# permissions
permissions_get_competition = lib.permissions_get_competition
permissions_get_competition.argtypes = [c_void_p]
permissions_get_competition.restype = c_char_p

permissions_print = lib.permissions_print
permissions_print.argtypes = [c_void_p]

permissions_has_action = lib.permissions_has_action
permissions_has_action.argtypes = [c_void_p, c_char_p]
permissions_has_action.restype = c_bool

# service
auth_service_new = lib.auth_service_new
auth_service_new.restype = c_void_p

auth_service_delete = lib.auth_service_delete
auth_service_delete.argtypes = [c_void_p]

auth_service_create = lib.auth_service_create
auth_service_create.argtypes = [c_char_p, c_char_p]
auth_service_create.restype = c_void_p

# version
bynd_libauth_version_print_full = lib.bynd_libauth_version_print_full
bynd_libauth_version_print_version_id = lib.bynd_libauth_version_print_version_id
bynd_libauth_version_print_version_name = lib.bynd_libauth_version_print_version_name
