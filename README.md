## Monero Wallet cli Wrapper

Quick python wrapper around monero-wallet-cli binary  
Using asyncio and subprocess  

- The goal of this project is to make it easier to handle your wallets with speed and safety 
- You can run a flask api along this and put it on a server now you can make transctions from an api
- first task "pro" restores a wallet using it's seed from specific height of your choice  
- Second task "pro2" runs command of your choice like sweep_all  
  check out offical docs for more commands
- Don't use the bin from this repo if you don't trust me get your own from offical repo
- if you are running this on a cloud server don't download the offical tarball containing the bins some of them is detected as malware
- if you liked this project consider supporting XMR address below

you can see random `print()` they act as break points so you can debug where it stopped  
## Example
Restoring wallet from seed and transfering all funds to another wallet (code found in automate.py)  

here's a sample output:  


```bash
./monero-wallet-cli
if
ii
b'This is the command line monero wallet. It needs to connect to a monero\n'
if
ii
b'daemon to work correctly.\n'
if
ii
b'WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.\n'
if
ii
b'\n'
if
ii
b"Monero 'Fluorine Fermi' (v0.18.2.2-release)\n"
if
ii
out
b'WARNING: You may not have a high enough lockable memory limit, see ulimit -l\n'
b'Generated new wallet: 44qLCs9UkgTMXSMd00000000000000000000000000000000000000000000000yrHxdu35b4zAyri6Hfnmhm\n'
b'View key: 0000000000000000000000000000000000000067e4fb10bd94078ab100\n'
is
ii
b'**********************************************************************\n'
is
ii
b'Your wallet has been generated!\n'
is
ii
b'To start synchronizing with the daemon, use the "refresh" command.\n'
is
ii
b'Use the "help" command to see a simplified list of available commands.\n'
is
ii
b'Use "help all" command to see the list of all available commands.\n'
is
ii
b'Use "help <command>" to see a command\'s documentation.\n'
is
ii
b'Always use the "exit" command when closing monero-wallet-cli to save \n'
is
ii
b"your current session's state. Otherwise, you might need to synchronize \n"
is
ii
b'your wallet again (your wallet keys are NOT at risk in any case).\n'
is
ii
b'\n'
is
ii
b'\n'
is
ii
b'NOTE: the following 25 words can be used to recover access to your wallet. Write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.\n'
is
ii
b'\n'
is
ii
b'nner against smelting\n'
is
ii
b' hiker ourselves duets hickory\n'
is
ii
b'jeers sidekick sifting ourselves\n'
is
ii
b'**********************************************************************\n'
is
ii
b'Warning: using an untrusted daemon at xmr-node.cakewallet.com:18081\n'
is
ii
b'Using a third party daemon can be detrimental to your security and privacy\n'
is
ii
b'Using your own without SSL exposes your RPC traffic to monitoring\n'
is
ii
b'You are strongly encouraged to connect to the Monero network using your own daemon\n'
is
ii
b'If you or someone you trust are operating this daemon, you can use --trusted-daemon\n'
is
ii
b'Using an untrusted daemon, skipping background mining check\n'
is
ii
b'If you are new to Monero, type "welcome" for a brief overview.\n'
is
ii
it
3i
b'Height 2851001 / 2875894\rHeight 2861000 / 2875894\rHeight 2870997 / 2875894\rHeight 2875721 / 2875894\rHeight 2875858 / 2875894\r\rHeight 2875881, txid <ae068330d5a5c212fdd010000000000000000000062efb0000bb8e9>, 0.000150000000, idx 0/0\n'
it
3i
b'Height 2875881 / 2875894\r\r                                                                \rRefresh done, blocks received: 173\n'
REFRESHISDONE
b'Untagged accounts:\n'
b'          Account               Balance      Unlocked balance                 Label\n'
b' *       0 44qLCs        0.000150000000        0.000150000000       Primary account\n'
i
ii
b'------------------------------------------------------------------------------------\n'
i
ii
b'          Total          0.000150000000        0.000150000000\n'
i
ii
b'Currently selected account: [0] Primary account\n'
i
ii
b'Tag: (No tag assigned)\n'
i
ii
b'Balance: 0.000150000000, unlocked balance: 0.000150000000\n'
i
ii
b'Background refresh thread started\n'
DONEEE!
if
ii
b'This is the command line monero wallet. It needs to connect to a monero\n'
if
ii
b'daemon to work correctly.\n'
if
ii
b'WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.\n'
if
ii
b'\n'
if
ii
b"Monero 'Fluorine Fermi' (v0.18.2.2-release)\n"
if
ii
b'Logging to ./monero-wallet-cli.log\n'
if
ii
b'WARNING: You may not have a high enough lockable memory limit, see ulimit -l\n'
if
ii
b'Opened wallet: 44qLCs000000000000000000000000000000000000000000000000000000000000000000000000ABgtyrHxdu35b4zAyri6Hfnmhm\n'
if
ii
b'**********************************************************************\n'
if
ii
b'Use the "help" command to see a simplified list of available commands.\n'
if
ii
b'Use "help all" to see the list of all available commands.\n'
if
ii
b'Use "help <command>" to see a command\'s documentation.\n'
if
ii
b'**********************************************************************\n'
if
ii
b'Warning: using an untrusted daemon at xmr-node.cakewallet.com:18081\n'
if
ii
b'Using a third party daemon can be detrimental to your security and privacy\n'
if
ii
b'Using your own without SSL exposes your RPC traffic to monitoring\n'
if
ii
b'You are strongly encouraged to connect to the Monero network using your own daemon\n'
if
ii
b'If you or someone you trust are operating this daemon, you can use --trusted-daemon\n'
out
iff
ii
b'\n'
iff
ii
b'Transaction 1/1:\n'
iff
ii
b'Spending from address index 0\n'
out2
ifff
ii
b'\n'
ifff
ii
b'Sweeping 0.000150000000 for a total fee of 0.000030640000.  Is this okay?  (Y/Yes/N/No): Transaction successfully submitted, transaction <c30c9f3fe6baf046908ab81996fa4a1e473a553baa6bc54f01d7a0b190f17b90>\n'
b'You can check its status by using the `show_transfers` command.\n'
b''
b''
[None]
```


## Donate

- xmr: `433CbZXrdTBQzESkZReqQp1TKmj7MfUBXbc8FkG1jpVTBFxY9MCk1RXPWSG6CnCbqW7eiMTEGFgbHXj3rx3PxZadPgFD3DX`
