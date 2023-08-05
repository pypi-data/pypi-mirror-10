'''
HTTP app with auto scaling, ELB and DNS
'''

from clickclick import warning, error
import pystache

from ._helper import prompt, check_security_group, check_iam_role, get_mint_bucket_name


TEMPLATE = '''
# basic information for generating and executing this definition
SenzaInfo:
  StackName: {{application_id}}
  Parameters:
    - ImageVersion:
        Description: "Docker image version of {{ application_id }}."

# a list of senza components to apply to the definition
SenzaComponents:

  # this basic configuration is required for the other components
  - Configuration:
      Type: Senza::StupsAutoConfiguration # auto-detect network setup

  # will create a launch configuration and auto scaling group with scaling triggers
  - AppServer:
      Type: Senza::TaupageAutoScalingGroup
      InstanceType: {{ instance_type }}
      SecurityGroups:
        - app-{{application_id}}
      IamRoles:
        - app-{{application_id}}
      ElasticLoadBalancer: AppLoadBalancer
      TaupageConfig:
        runtime: Docker
        source: "{{ docker_image }}:{{=<% %>=}}{{Arguments.ImageVersion}}<%={{ }}=%>"
        ports:
          {{http_port}}: {{http_port}}
        mint_bucket: "{{ mint_bucket }}"

  # creates an ELB entry and Route53 domains to this ELB
  - AppLoadBalancer:
      Type: Senza::WeightedDnsElasticLoadBalancer
      HTTPPort: {{http_port}}
      HealthCheckPath: {{http_health_check_path}}
      SecurityGroups:
        - app-{{application_id}}-lb
'''


def gather_user_variables(variables, region):
    prompt(variables, 'application_id', 'Application ID', default='hello-world')
    prompt(variables, 'docker_image', 'Docker image', default='stups/hello-world')
    prompt(variables, 'http_port', 'HTTP port', default=8080, type=int)
    prompt(variables, 'http_health_check_path', 'HTTP health check path', default='/')
    prompt(variables, 'instance_type', 'EC2 instance type', default='t2.micro')
    prompt(variables, 'mint_bucket', 'Mint S3 bucket name', default=lambda: get_mint_bucket_name(region))

    http_port = variables['http_port']

    sg_name = 'app-{}'.format(variables['application_id'])
    rules_missing = check_security_group(sg_name, [('tcp', 22), ('tcp', http_port)], region, allow_from_self=True)

    if ('tcp', 22) in rules_missing:
        warning('Security group {} does not allow SSH access, you will not be able to ssh into your servers'.format(
            sg_name))

    if ('tcp', http_port) in rules_missing:
        error('Security group {} does not allow inbound TCP traffic on the specified HTTP port ({})'.format(
            sg_name, http_port
        ))

    rules_missing = check_security_group(sg_name + '-lb', [('tcp', 443)], region)

    if rules_missing:
        error('Load balancer security group {} does not allow inbound HTTPS traffic'.format(sg_name))

    check_iam_role(variables['application_id'], variables['mint_bucket'], region)

    return variables


def generate_definition(variables):
    definition_yaml = pystache.render(TEMPLATE, variables)
    return definition_yaml
