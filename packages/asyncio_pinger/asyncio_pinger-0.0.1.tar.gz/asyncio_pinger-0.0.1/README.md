# Pinger

*Pinger* based on asyncio library.

*Pinger* find servers pings and show it in reversed order (first with worst
ping, last with best ping).

## Instalation

```bash

pip install asyncio_pinger

```

## Usage

Create file like this:

```txt

Argentina, Buenos Aires (PPTP/L2TP): bn-ar.boxpnservers.com
Argentina, Buenos Aires (SSTP): sstp-bn-ar.boxpnservers.com

...

```

Run Python

```python

from asyncio_pinger import Pinger

p = Pinger(path_to_file)
p.run()
p.print_results()

```
