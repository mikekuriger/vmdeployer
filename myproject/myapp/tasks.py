# myapp/tasks.py
from background_task import background
from myapp.models import Deployment
from django.conf import settings
from django.core.mail import send_mail
import subprocess
import os

#@background(schedule=300)  # delay 5 minutes before running (first time)
@background
def check_queued_deployments():
    queued_deployments = Deployment.objects.filter(status='queued')
    source_path = settings.MEDIA_ROOT
    base_path = settings.BASE_DIR

    # if not source_path.exists():
    #     print(f"Source file {source_path} not found.")
    #     return

    # Retrieve all queued deployments
    queued_deployments = Deployment.objects.filter(status='queued')

    # Loop through each deployment and run the deploy script
    for deployment in queued_deployments:
        deployment_name = deployment.deployment_name
        print(deployment_name)
        deploy_command = ["python", f"{base_path}/myapp/deploy.py", deployment_name]
        print(deploy_command)

        try:
            # Run the deploy script and wait for it to finish
            subprocess.run(deploy_command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            
        except subprocess.CalledProcessError as e:
            print(f"Error deploying {deployment_name}: {e.stderr.decode('utf-8')}")

            
@background
def send_failure_alert():
    failed_deployments = Deployment.objects.filter(status='failed')
    
    if failed_deployments.exists():
        deployment_names = ", ".join([d.deployment_name for d in failed_deployments])
        subject = "Alert: Failed SSVM Deployment {deployment_names}"
        message = f"The following deployments have failed: {deployment_names}"
        recipient_list = ['mk7193@thryv.com'] 
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )