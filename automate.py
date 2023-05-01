import os, random
import asyncio, subprocess


height = "2875721" #@param {type:"string"}
seed = "water lopped sayings hookup slug befit outbreak hence gourmet gambit eggs reruns assorted huge coffee unknown pause evicted zero obvious zesty army jellyfish jockey jellyfish" #@param {type:"string"}

# adjust your cli path
path = "./"

# add .exe if on windows
cmd = path + "monero-wallet-cli"
print(cmd) #debug path
waln = f"mir{random.randint(1, 999999)}" #random wallet name

async def run():
    # we are using cake wallet node
    pro = await asyncio.create_subprocess_exec(cmd, '--daemon-address', 'xmr-node.cakewallet.com:18081', '--restore-from-seed', '--electrum-seed', seed, '--restore-height', height, '--generate-new-wallet', waln, '--password', '', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while 1:
        await asyncio.sleep(0.1)
        print("if")
        o  = await pro.stdout.readline()
        print("ii")
        if "Logging to" in str(o):
            break
        elif len(str(o)) == 0:
            print(o)
            break
        else:
            print(o)
            continue

    print("out")
    pro.stdin.write(b'\n') # press enter (skip seed offset)
    await pro.stdin.drain()
    print(await pro.stdout.readline())
    print(await pro.stdout.readline())
    print(await pro.stdout.readline())
    while 1: # detect block sync
        await asyncio.sleep(0.1)
        print("is")
        o  = await asyncio.wait_for(pro.stdout.readline(), timeout=1.0)
        print("ii")
        if "Starting refresh..." in str(o):
            break
        elif len(str(o)) == 0:
            print(o)
            break
        else:
            print(o)
            pro.stdin.write(b'\n')
            await pro.stdin.drain()
            continue

    while 1: ## wait for refreshing to finish!
        await asyncio.sleep(0.1)
        print("it")
        try:
          o = await asyncio.wait_for(pro.stdout.readline(), timeout=1.0)
          print("3i")
          if len(o) == 0: raise("err")
          print(o)
          if "Starting refresh..." in str(o): continue
          if "\\rRefresh done," in str(o): break
        except: # press enter untill refresh is done
          await asyncio.sleep(1)
          print("tryingENTER")
          pro.stdin.write(b'\n')
          await pro.stdin.drain()
          print("tryingENTERSUC")

    print("REFRESHISDONE")
    pro.stdin.write(b'exit\n')
    await pro.stdin.drain()
    print(await pro.stdout.readline())
    print(await pro.stdout.readline())
    print(await pro.stdout.readline())
    while 1:
        await asyncio.sleep(0.1)
        print("i")
        o  = await pro.stdout.readline()
        print("ii")
        if "[wallet" in str(o) or "Background refresh" in str(o):
            print(o)
            break
        elif len(str(o)) == 0:
            print(o)
            break
        else:
            print(o)
            continue
    print("DONEEE!")

    try:
        pro.stdin.write(b'exit\n')
        await pro.stdin.drain()
        print(await pro.stdout.readline())
    except: pass

    await pro.wait()  # Wait for the process to complete
    if pro.returncode:
        print(f"Process exited with return code {pro.returncode}")

    # Wallet is created now we run whatever commands
    # replace your cmd in the next line
    pro2 = await asyncio.create_subprocess_exec(cmd, '--daemon-address', 'xmr-node.cakewallet.com:18081', '--wallet',  waln, '--password', '', "--command", "sweep_all", "433CbZXrdTBQzESkZReqQp1TKmj7MfUBXbc8FkG1jpVTBFxY9MCk1RXPWSG6CnCbqW7eiMTEGFgbHXj3rx3PxZadPgFD3DX", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while 1:
        await asyncio.sleep(0.1)
        print("if")
        o  = await pro2.stdout.readline()
        print("ii")
        if "operating this daemon" in str(o):
            print(o)
            break
        elif len(str(o)) == 0:
            print(o)
            break
        else:
            print(o)
            continue

    print("out")
    pro2.stdin.write(b'\n') #enter empty password
    await pro2.stdin.drain()
    while 1:
        await asyncio.sleep(0.1)
        print("iff")
        o  = await pro2.stdout.readline()
        print("ii")
        if "Spending from" in str(o):
            print(o)
            break
        elif len(str(o)) == 0:
            print(o)
            break
        else: 
            print(o)
            continue
    print("out2")
    pro2.stdin.write(b'Y\n') #yes
    await pro2.stdin.drain()
    while 1:
        await asyncio.sleep(0.1)
        print("ifff")
        o  = await pro2.stdout.readline()
        print("ii")
        if "Is this okay?" in str(o):
            print(o)
            break
        elif len(str(o)) == 0:
            print(o)
            break
        else: 
            print(o)
            continue
    print(await pro2.stdout.readline())
    print(await pro2.stdout.readline())
    print(await pro2.stdout.readline())

#await asyncio.gather(run()) #run in colab
asyncio.run(run())
