# Axis and Allies Probability Simulator

This Python package runs many simulations of Axis and Allies battles and keeps track of which side wins each time.

## Full Documentation

[Documentation Index](docs/axisandallies/index.md)

## Running

**Step 1**: Add `yaml` files to the `battles` directory.

File format example:
```yaml
attacker:
    I: 4
    F: 2
defender:
    I: 2
    F: 2
```

**Step 2**:

```zsh
$ make
```

**Step 3**:

Open `.txt` files in the `battles` directory to read the reports.

## To-Do

- [ ] Implement command line entry of numbers of units.
- [ ] See if there is a correlation between the total hit dice of each side or the difference between them to determine if we can create a rule of thumb for decision making.
- [ ] Get tests working. The imports are a bitch.
- [ ] Add some type hints and a type checking package.
- [x] Figure out why adding a bomber to defenders decreases their win probability.

## Implemented Units

- Infantry (I)
- Armor (A)
- Fighter (F)
- Bomber (B)

## Non-Implemented Units

- AA Guns (AA)
- Battleships (BB)
- Aircraft Carriers (AC)
- Transports (T)
- Submarines (S)

## Future Features

- Naval battles
- Special rules for:
  - Battleships in support of landings.
  - Submarines.
  - AA guns.
