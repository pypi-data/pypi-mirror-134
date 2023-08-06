"""
HTTP Status Codes
"""
HTTP_OK = 200
HTTP_CREATED = 202
HTTP_DELETE = 204
HTTP_NOT_AUTHORIZED = 401
HTTP_NOT_FOUND = 404
HTTP_UNPROCESSABLE_ENTITY = 422
HTTP_TOO_MANY_REQUESTS = 429
HTTP_INTERNAL_ERROR = 500

"""
Digital Ocean Resource Endpoints
"""
BASE_URL = 'https://api.digitalocean.com/v2'
DROPLET_URL = "/droplets"
REGIONS_URL = "/regions"
SIZES_URL = "/sizes"

"""
Image Constants
"""
VALID_IMAGE_TYPES = ['base', 'snapshot', 'backup', 'custom','admin']
VALID_DIST_TYPES = ['Arch Linux', 'CentOS', 'CoreOS', 'Debian', 'Fedora',
    'Fedora Atomic', 'FreeBSD', 'Gentoo', 'openSUSE', 'RancherOS', 'Ubuntu', 'Unknown']
VALID_IMAGE_STATUS = ['NEW', 'new', 'available', 'pending','deleted','retired']

"""
Droplet Constants
"""
VALID_DOPLET_STATUS = ["new", "active", "off", "archive"]
