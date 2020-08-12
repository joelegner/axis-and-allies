# Axis and Allies Probability Simulator

This Python package runs many simulations of Axis and Allies battles and keeps track of which side wins each time.

To run do either of the following.

```zsh
$ pipenv shell
$ python axisandallies
```

Or

```zsh
$ pipenv run python axisandallies
```

## To-Do

- [ ] Implement command line entry of numbers of units.
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
