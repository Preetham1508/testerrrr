cardholder:
  enableAtroposEbs:
    inDeployment: true
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: eks.amazonaws.com/nodegroup
                operator: In
                values:
                - aws-default-pp-mumbai-businessapp-4x-v1
                - aws-default-pp-mumbai-businessapp-4x-v2
  hpa:
    cpu: 80
    enabled: true
    maxReplicas: 15
  httpHealthCheckServiceMonitor:
    enabled: true
    targets:
    - name: healthcheck
      url: https://acropolis-pci.internal.mum1-pp.zetaapps.in/cardholder/health
priorityClassName: acropolis-pci-priority
  replicaCount: 2
  resources:
    limits:
      cpu: 2000m
      memory: 2000Mi
    requests:
      cpu: 1000m
      memory: 1500Mi
