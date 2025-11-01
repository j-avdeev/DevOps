flowchart LR
    subgraph CP["Control Plane (cp) nodes"]
        subgraph API["kube-apiserver"]
        end

        ETCD[(etcd)]
        KCM["kube-controller-manager"]
        KS["kube-scheduler"]
        CCM["cloud-controller-manager"]
        KubeletCP["kubelet"]
        KProxyCP["kube-proxy"]

        KCM --> API
        KS --> API
        API --> ETCD
        CCM -.-> API
        API --> KubeletCP
        API --> KProxyCP
    end

    subgraph Worker1["Worker Node 1"]
        Kubelet1["kubelet"]
        KProxy1["kube-proxy"]
        Containerd1["containerd"]
        Net1["iptables / eBPF"]
        Pods1[("Pods")]

        Kubelet1 --> Containerd1
        KProxy1 --> Net1
        Containerd1 --> Pods1
    end

    subgraph Worker2["Worker Node 2"]
        Kubelet2["kubelet"]
        KProxy2["kube-proxy"]
        Containerd2["containerd"]
        Net2["iptables / eBPF"]
        Pods2[("Pods")]

        Kubelet2 --> Containerd2
        KProxy2 --> Net2
        Containerd2 --> Pods2
    end

    subgraph Worker3["Worker Node 3"]
        Kubelet3["kubelet"]
        KProxy3["kube-proxy"]
        Containerd3["containerd"]
        Net3["iptables / eBPF"]
        Pods3[("Pods")]

        Kubelet3 --> Containerd3
        KProxy3 --> Net3
        Containerd3 --> Pods3
    end

    CLI["kubectl / API call (curl)"] --> API

    API --> Kubelet1
    API --> KProxy1
    API --> Kubelet2
    API --> KProxy2
    API --> Kubelet3
    API --> KProxy3

    style API fill:#fef3c7,stroke:#facc15,stroke-width:2px
    style ETCD fill:#e0e7ff,stroke:#6366f1,stroke-width:2px
    style Worker1 fill:#ecfdf5,stroke:#10b981
    style Worker2 fill:#ecfdf5,stroke:#10b981
    style Worker3 fill:#ecfdf5,stroke:#10b981
    style CP fill:#f9fafb,stroke:#9ca3af
