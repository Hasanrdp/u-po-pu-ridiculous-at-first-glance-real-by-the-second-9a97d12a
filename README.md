# Certified Haunted

[![make.fun](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/Hasanrdp/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/Hasanrdp/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

Entry for the make.fun bounty **Ridiculous at First Glance, Real by the
Second**: one sentence, at most 200 characters, pitching a startup idea so
strange it sounds like a joke, yet specific enough that a reader can see the
customers and the money.

## The pitch

> We certify your Airbnb as haunted for $299, because guests pay 40% more to sleep where the reviews say the lights flicker by themselves.

A certification service that turns a haunted-house liability into a premium
listing: the host pays $299 for the certificate, the guests pay 40% more for
the night. Ridiculous at first glance — a real market on the second look.

## The program

`main.py` (Python 3.13, standard library only) writes the pitch above to
`/output/entry.txt`. It is fully deterministic: the same sentence, byte for
byte, on every run, with no network, no input and no randomness. After
writing, it reads the file back and asserts it matches the pitch exactly and
stays inside the 1–200 character gate (136 characters).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
