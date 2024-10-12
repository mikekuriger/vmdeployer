from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Deployment(models.Model):
    deployment_date = models.CharField(max_length=255)
    deployment_name = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    full_hostnames = models.CharField(max_length=255)
    ticket = models.CharField(max_length=50)
    appname = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)        # used for deployment name - uid
    owner_value = models.CharField(max_length=255)  # used for display - first last (uid)
    datacenter = models.CharField(max_length=50)
    server_type = models.CharField(max_length=50)        # lnt
    server_type_value = models.CharField(max_length=50)  # Testing
    deployment_count = models.IntegerField()
    cpu = models.IntegerField()
    ram = models.IntegerField()
    os = models.CharField(max_length=50)           # template name
    os_value = models.CharField(max_length=50)     # long name
    disk_size = models.IntegerField()
    add_disks = models.BooleanField()
    additional_disk_size = models.IntegerField(null=True, blank=True)
    mount_path = models.CharField(max_length=50, null=True, blank=True)
    cluster = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    nfs_home = models.BooleanField()
    join_centrify = models.BooleanField()
    centrify_zone = models.CharField(max_length=50, null=True, blank=True)
    centrify_role = models.CharField(max_length=50,null=True, blank=True)
    install_patches = models.BooleanField()
    status = models.CharField(max_length=20, default='queued')  # for tracking status
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hostname} - {self.status}"
