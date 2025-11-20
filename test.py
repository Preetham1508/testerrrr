axon-admin-user-service-api:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: schedule-on
            operator: In
            values:
            - business-app-subnet
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - axon-admin-user-service-api
          topologyKey: eks.amazonaws.com/capacityType
        weight: 100
  clusterName: axoncore
  enabled: true
  deployment:
    additionalAnnotations:
      axon.zetapay.tech/recyle-pod: "true"
      axon.zetapay.tech/restart-schedule: "0 11 * * 0"
  envProperties:
    API_BASEURL: https://axoncore.internal.us2-axon.zetapay.tech/axon-admin-user-service-api/
    CERTSTORE_PROTEUS_ENDPOINT: https://axoncipher.zone.olympus.infra/proteus/zeta.in/
    CRUX_LLT_GOD_OAUTH_APP_AUTH_PROFILE_ID: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.app-auth-profile-id
    CRUX_LLT_GOD_OAUTH_APP_PRIVATE_KEY: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.app-private-key
    CRUX_LLT_GOD_OAUTH_APP_PUBLIC_KEY: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.app-public-key
    CRUX_LLT_GOD_OAUTH_APP_RESOURCE_CERT: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.app-resource-cert
    CRUX_LLT_GOD_OAUTH_CLIENT_ID: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.client-id
    CRUX_LLT_GOD_OAUTH_CLIENT_SECRET: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.client-secret
    CRUX_LLT_GOD_OAUTH_DOMAIN_ID: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.domain-id
    CRUX_LLT_GOD_OAUTH_SCOPE: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/tenants/0/auth#crux-llt.god.oauth.scope
    CRUX_LLT_TOKEN_BUFFER_TIME: 3000
    DELTA_V2_ENCRYPTION_BASE64SECRET: vault:secrets/data/zone/common/delta#delta.v2.encryption.base64Secret
    DELTA_V2_URL: vault:secrets/data/zone/common/delta#delta.v2.url
    ENABLE_LOGBOOK_REQUEST_LOG: false
    ENABLE_LOGBOOK_RESPONSE_LOG: false
    ENABLE_REQUEST_ACCESS_LOG: false
    ENVIRONMENT: prod
    JMX_PORT: 55555
    JMX_PROMETHEUS_JAVAAGENT_CONFIG_FILE: /prometheus/jmx-exporter-config.yaml
    JMX_PROMETHEUS_JAVAAGENT_ENABLED: true
    JMX_PROMETHEUS_JAVAAGENT_METRICS_PORT: 44444
    JMX_RMI_PORT: 55555
    JOLOKIA_JAVAAGENT_ENABLED: true
    KINESIS_ACCESSKEY: vault:secrets/data/zone/common/logging#KINESIS_ACCESSKEY
    KINESIS_REGION: vault:secrets/data/zone/common/logging#KINESIS_REGION
    KINESIS_SECRETKEY: vault:secrets/data/zone/common/logging#KINESIS_SECRETKEY
    OTEL_ENABLED: true
    OTEL_EXTENSIONS_ENABLED: true
    POSTGRES_JDBC_PASSWORD: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/application#POSTGRES_JDBC_PASSWORD
    POSTGRES_JDBC_URL: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/application#POSTGRES_JDBC_URL
    POSTGRES_JDBC_USERNAME: vault:secrets/data/cluster/axoncore/axon-admin-user-service-api/application#POSTGRES_JDBC_USERNAME
    PROTEUS_ENDPOINT: https://axoncipher.zone.olympus.infra/proteus/zeta.in/
    SERVER_TOMCAT_MIN-SPARE-THREADS: 32
    SERVER_MAX_HTTP_REQUEST_HEADER_SIZE: 1MB
    SESSIONS_PROTEUS_ENDPOINT: https://axoncipher.zone.olympus.infra/proteus/zeta.in/
    SPRINGDOC_APIDOCS_ENABLED: false
    SPRINGDOC_SWAGGERUI_CONFIGURL: /axon-admin-user-service-api/v3/api-docs/swagger-config
    SPRINGDOC_SWAGGERUI_ENABLED: false
    SPRINGDOC_SWAGGERUI_URL: /axon-admin-user-service-api/v3/api-docs/
    SSO_BASE_URL: https://axoncipher.zone.olympus.infra/sso/
    TENANT_ONBOARDED_IDS: 1000001,0
    javaXms: 1536M
    javaXmx: 1536M
    LOGGING_PIPELINE: KINESIS_AND_SOUT
    METRIC_LOG_FORMAT: JSON
    DB_JDBC_CONNECTION_MAXIDLEFACTOR: 1
    DB_JDBC_CONNECTION_POOLSIZEFACTOR: 1
    DB_JDBC_DATASOURCE_TYPE: APACHE_DBCP
    DB_THREAD_POOL_FACTOR: 1
    ADMIN_USER_OPENSEARCH_INDEX_NAME: axon-fi-user
    CLUSTER_NAME: axoncore
    OPENSEARCH_AWSIAMROLEARN: arn:aws:iam::683738265913:role/zeta-aws-use2-axon-prod-pci-apm-europa-crud-role
    OPENSEARCH_AWSIAMROLESESSIONNAME: TES-SESSION
    OPENSEARCH_AWSREGION: us-east-2
    OPENSEARCH_AWSSERVICENAME: es
    OPENSEARCH_ENABLED: true
    OPENSEARCH_HOSTS: vpc-axon-prod-pci-apm-europa-tbhsrksvdfokpmx2sflxti5ype.us-east-2.es.amazonaws.com:-1
    TENANT_ID: "1000001"
    OPENSEARCH_SYNC_DELETE_BATCH_SIZE: 500
    OPENSEARCH_SYNC_SYNC_BATCH_SIZE: 2000
    USER_VIEW_HISTORY_MAX_AGE: 90
    OPENSEARCH_HARD_DELETE_ON_ALL_DATA_ENABLED: true
    OPENSEARCH_BULK_SYNC_ENABLED: true
    GARBAGE_COLLECTOR: G1GC
    JAVA_EXTRA_OPTS: >-
      -XX:+UseG1GC 
      -XX:G1ReservePercent=10 
      -XX:InitiatingHeapOccupancyPercent=45
      -XX:NewRatio=5
      -XX:+UseStringDeduplication
      -XX:+ParallelRefProcEnabled
      -XX:MaxGCPauseMillis=200
  envs:
  - name: environmentName
    value: production
  resources:
    limits:
      ephemeral-storage: "3Gi"
      memory: 2048Mi
    requests:
      cpu: 1.0
      ephemeral-storage: "3Gi"
      memory: 2048Mi
  replicaCount: 2
  hpa:
    additionalAnnotations:
      "axon.zetapay.tech/enable-scheduled-scaling": "true"
      "axon.zetapay.tech/scheduled-time-scale-down": "30 2 * * *"
      "axon.zetapay.tech/scheduled-replica-count-scale-down": "2"
      "axon.zetapay.tech/scheduled-time-scale-up": "30 11 * * *"
      "axon.zetapay.tech/scheduled-replica-count-scale-up": "3"
    cpu: 70
    enabled: true
    maxReplicas: 4
  image:
    pullPolicy: IfNotPresent
    repository: 813361731051.dkr.ecr.ap-south-1.amazonaws.com
    repositoryPath: axon-admin-user-service-api
  ingress:
    enabled: false
  olympusLabels:
    olympusCluster: axoncore
    olympusClusterBU: axon
    olympusClusterTeam: axon
    olympusZone: zeta-aws-use2-axon-prod-pci-eks-01
    olympusZoneEnv: production
  prometheus:
    custom_rules:
      alerts: []
      name: custom
    labels: {}
    oms_health_check:
      custom_alerts: []
      pod:
        enable: false
      probe:
        enable: false
      probe_absent:
        enable: true
      up:
        enable: false
      up_absent:
        enable: true
    oms_rules:
      custom_alerts: []
      jvm_memory:
        enable: true
      thread_count:
        enable: true
    ops_rules:
      custom_alerts: []
      image_pull_backoff:
        enable: false
    spingboot_health_check:
      custom_alerts: []
      pod:
        enable: false
      probe:
        enable: false
      probe_absent:
        enable: true
      up:
        enable: false
      up_absent:
        enable: true
    serviceHealthAlerts:
      restartThresholdWarn: 1
      memoryThresholdWarn: 75
      cpuThresholdWarn: 70
      grafana_url: https://grafana.internal.us2-axon.zetapay.tech/d/cel8qs7fo1wqod/axon-service-health-check
    spingboot_rules:
      custom_alerts: []
      http4xx:
        enable: false
      http5xx:
        enable: false
      jvm_cpu:
        enable: false
      jvm_high_latency:
        enable: false
      jvm_high_requests:
        enable: false
      jvm_memory:
        enable: false
  service:
    healthCheckPath: /status
    livenessProbeInitialDelaySeconds: 5
    readinessProbeInitialDelaySeconds: 15
    targetPort: 8080
    annotations: {
        "ingress.kubernetes.io/service-upstream": "true"
      }
  serviceAccountName: axon-admin-user-service-api
  serviceAccount:
    additionalAnnotations:
      eks.amazonaws.com/role-arn: arn:aws:iam::683738265913:role/zeta-aws-use2-axon-prod-pci-apm-europa-crud-role
      eks.amazonaws.com/sts-regional-endpoints: 'true'
  serviceMonitor:
    enabled: true
    monitors:
    - interval: 60s
      labels:
        prometheus: zone-monitoring
      matchLabels:
        app.kubernetes.io/name: axoncore
      name: jmxmetrics
      namespace: axoncore
      path: /prometheus
      port: jmxmetrics
      scrapeTimeout: 30s
  atroposTopics:
    topic-1:
      crName: subscription-admin-user-opensearch-sync-created-v1
      name: _tenant_1000001_adminUserSync
      tenantID: "1000001"
      tenantCode: fis
  atroposSubscriptions:
    enableV2: true
    subscription-1:
      crName: subscription-adminuser-opensearch-sync-created-v1
      state: ACTIVE
      subscriptionType: WEBHOOK
      config:
        subscriber: "axoncore"
        trace.enable: "true"
        request.timeout.ms: '15000'
      eventName: adminUserSync_CREATED
      subscriber: "axoncore"
      subscriptionID: subscription_1000001_adminUserSync
      tenantID: "1000001"
      topic: _tenant_1000001_adminUserSync
      transformerJS: function transform(payload, sender) { return JSON.stringify(payload);}
      webhookURL: https://axoncore.zone.olympus.infra/axon-admin-user-service-api/v1/tenants/1000001/webhooks/opensearch/users/sync
      tenantCode: fis
