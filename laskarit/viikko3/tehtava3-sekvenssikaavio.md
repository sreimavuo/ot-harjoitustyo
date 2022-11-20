# Tehtävä 3: Sekvenssikaavio

Tarkastellaan bensatankista ja moottorista koostuvan koneen Python-koodia.

Piirrä sekvenssikaaviona tilanne, jossa kutsutaan (jostain koodin ulkopuolella olevasta metodista) ensin Machine-luokan konstruktoria ja sen jälkeen luodun `Machine`-olion metodia `drive`.

Muista, että sekvenssikaaviossa tulee tulla ilmi kaikki mainin suorituksen aikaansaamat olioiden luomiset ja metodien kutsut!

## Sekvenssikaavio

```mermaid
sequenceDiagram
participant main
participant machine
participant tank
participant engine
main->>machine: Machine()
machine->>tank: FuelTank()
machine->>tank: fill(40)
machine->>engine: Engine(tank)
main->>machine: drive()
machine->>engine: start()
engine->>tank: consume(5)
machine->>engine: use_energy()
engine->>tank: consume(10)
```

Tehtävässä ei määritelty kuinka monta kertaa `drive`-metodia kutsutaan, joten oletin että kerran.
