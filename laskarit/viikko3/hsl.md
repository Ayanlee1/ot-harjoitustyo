## HSL-matkakortti, sekvenssikaavio

```mermaid
sequenceDiagram
    participant main
    participant HKLLaitehallinto
    participant Lataajalaite
    participant Lukijalaite
    participant Kioski
    participant Matkakortti
    
    main->>HKLLaitehallinto: __init__()
    activate HKLLaitehallinto
    HKLLaitehallinto-->>main: laitehallinto
    deactivate HKLLaitehallinto
    

    main->>Lataajalaite: __init__()
    activate Lataajalaite
    Lataajalaite-->>main: rautatietori
    deactivate Lataajalaite
    

    main->>Lukijalaite: __init__()
    activate Lukijalaite
    Lukijalaite-->>main: ratikka6
    deactivate Lukijalaite
    

    main->>Lukijalaite: __init__()
    activate Lukijalaite
    Lukijalaite-->>main: bussi244
    deactivate Lukijalaite
    

    main->>HKLLaitehallinto: lisaa_lataaja(rautatietori)
    activate HKLLaitehallinto
    HKLLaitehallinto-->>main: 
    deactivate HKLLaitehallinto
    

    main->>HKLLaitehallinto: lisaa_lukija(ratikka6)
    activate HKLLaitehallinto
    HKLLaitehallinto-->>main: 
    deactivate HKLLaitehallinto
    
    main->>HKLLaitehallinto: lisaa_lukija(bussi244)
    activate HKLLaitehallinto
    HKLLaitehallinto-->>main: 
    deactivate HKLLaitehallinto
    

    main->>Kioski: __init__()
    activate Kioski
    Kioski-->>main: lippu_luukku
    deactivate Kioski
    
    main->>Kioski: osta_matkakortti("Kalle")
    activate Kioski
    Kioski->>Matkakortti: __init__("Kalle")
    activate Matkakortti
    Matkakortti-->>Kioski: uusi_kortti
    deactivate Matkakortti
    Kioski-->>main: kallen_kortti
    deactivate Kioski
    

    main->>Lataajalaite: lataa_arvoa(kallen_kortti, 3)
    activate Lataajalaite
    Lataajalaite->>Matkakortti: kasvata_arvoa(3)
    activate Matkakortti
    Matkakortti-->>Lataajalaite: 
    deactivate Matkakortti
    Lataajalaite-->>main: 
    deactivate Lataajalaite
    
    
    main->>Lukijalaite: osta_lippu(kallen_kortti, 0)
    activate Lukijalaite
    Lukijalaite->>Matkakortti: vahenna_arvoa(1.5)
    activate Matkakortti
    Matkakortti-->>Lukijalaite: 
    deactivate Matkakortti
    Lukijalaite-->>main: True
    deactivate Lukijalaite
    
    
    main->>Lukijalaite: osta_lippu(kallen_kortti, 2)
    activate Lukijalaite
    Lukijalaite-->>main: False
    deactivate Lukijalaite