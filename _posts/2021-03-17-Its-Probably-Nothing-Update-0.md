---
layout: post
author: sarco_builders
title: It's Probably Nothing Update 0
---
###### - - - - - - - - - - - - - - - - - - - -
## 0.1 Quick Update
###### - - - - - - - - - - - - - - - - - - - -

### What's happened so far on test

0. Everything, the [app](https://app.dev.sarcophagus.io/#/tomb) is live on testnet, see request for testing help below. 

### What's happened so far on main

0. [Fixed supply token minted](https://etherscan.io/token/0x7697b462a7c4ff5f8b55bdbc2f4076c2af9cf51a)
1. [Liquidity mining deployed, funded, and running](https://etherscan.io/address/0x7a9a0d2ae824ba57a5fe7dabaf7e6846021d4e8e)
2. [Builders vesting distribution contract funded and running](https://etherscan.io/address/0xe79a907147055fbc9dee9f337c5746271b045122)
3. [Aragon DAO voting proxy contract deployed](https://client.aragon.org/#/sarcophagus.aragonid.eth)
4. [DAO created and funded w/incentive allocations](https://client.aragon.org/#/sarcophagus/0x3299f6a52983ba00ffaa0d8c2d5075ca3f3b7991/)
5. [Uniswap ETH/SARCO pool small but chugging along](https://info.uniswap.org/token/0x7697b462a7c4ff5f8b55bdbc2f4076c2af9cf51a)

---

###### - - - - - - - - - - - - - - - - - - - -
## 0.2 Help Us Test Sarcophaugs on Hybrid Testnet
###### - - - - - - - - - - - - - - - - - - - -


There is a version of the Sarcophagus dApp at: [https://app.dev.sarcophagus.io/](https://app.dev.sarcophagus.io/) it runs on the Rinkeby ETH testnet and the Arweave mainnet (shout out to AR for being so cheap we can test on main). 

If you would like to help us test Sarcophagus please go to our [Discord](https://discord.gg/XPNKEZW) and request some testnet tokens. Someone will send you .01 ETH and 100 SARCO on the Rinkeby network. You can then connect your metammask to the app and try everything out! 

The rinkeby token address for the mock $SARCO is: [0x77ec161f6c2f2ce4554695a07e071d3f0ef3aef5](https://rinkeby.etherscan.io/token/0x77ec161f6c2f2ce4554695a07e071d3f0ef3aef5)

More explainations will be coming soon about limitations, but if you would like to do a quick and dirty test, here are the steps: 

0. Request testnet tokens from our discord and we will send you .01 ETH and 100 SARCO.

1. Set your metamask to rinkeby and connect to the dApp on the [create sarcophagus](https://app.dev.sarcophagus.io/#/create) page.

2. Get the extended public key for your recipient account by signing a message from it here: [https://app.dev.sarcophagus.io/#/publicKey](https://app.dev.sarcophagus.io/#/publicKey) 
If you don't want to deal with that, here's an ETH recipient keypair you can use: <br>
Extended Public Key:
`0x04451c509dee53b358c0261df187f150cdd354dff81ada711254d4f362c972866bf506b18d4a8817e1fae39c5c9dc0a4abeff17451e83dc5b66ab417d5015b80f4`<br>
Private Key: 
`0xff5793ccb2f2da317982a58b7b5d2a461ccc267f0a88fe07ac1efd1204fb04e4`

3. Next upload your file, the smaller the better for this alpha testing, but feel free to try whatever. Here's a [sample 155 byte .txt file]({{site.baseurl}}/assets/files/sarco_test_key.txt).

4. Set your resurrection time, please make sure this is at least a few hours away for the alpha. 

5. Chose an Archaeologist to curse, you're welcome to adjust the parameters, but the defaults are set to make sure everything runs smoothly.

6. Click "Finish" to create your sarcophagus.

7. You will need to approve the ERC20 SARCO token to be spent by the contract the first time, and then you can execute the transfer. 

8. Once the sarcophagus is created you will have to sign it one more time before it is finalized. 

9. You can now monitor/rewrap your sarcophagi in the Tomb. 

There is a good chance that you are going to encounter some errors. The best way to communicate those to the builders is to take a screenshot of the errors in the console + post in Discord. Even if no one responds WE STILL SEE IT AND LOVE YOU! In Chrome, right click the app page > Inspect > Console. If you don't mind, please include what you are trying to embalm and what setup you are using. 

Any and all feedback is appreciated, whether it's on twitter, discord, telegram, etc. However submitting an issue on GitHub is bar far the best way to help the builders fix any bugs or negative user experiences prior to mainnet launch. 

----
###### - - - - - - - - - - - - - - - - - - - -
## 0.3 Current + Future Incentives
###### - - - - - - - - - - - - - - - - - - - -


#### Currently Running:

### Liquidity Mining 
[mining.sarcophagus.io](https://mining.sarcophagus.io) stablecoin depositors have $SARCO distributed in proportion to their stake in the pool. 1m tokens are distributed equally over 1 year, started at 00:00 UTC Jan 13th, 2021.

##### Planned:

### Embalmer Matching Incentive

2m $SARCO allocated for user grants/incentives will be distributed to users who create and manage sarcophagi on the dApp in the first 30 days after mainnet launch. The distribution will be equal to the fees paid to the archaeologist by the embalmer, in the creation and management of sarcophagi. 

### Archaeologist Bonding Incentive

15m + 2m $SARCO allocated for archaeologist bonding + grants (a decision was made to combine grants and incentives due to legal / accounting troubles created by grants without consideration). 

The 17m $SARCO will be distributed per archaeologist in proportion to the amount of $SARCO bonded, over the course of one year, calculated per second. In short: the more an Archaeologist has bonded, for longer, the more they will earn.   

##### Planning:

### Uniwswap ETH/SARCO Pool Incentive

A plan to commit 2.5m $SARCO tokens from the DAO's treasury to incentivize liquidity on Uniswap. Likely in the form of an LP-Token lock linear release mechanism. This would work just like the current Liquidity Mining contract except instead of accepting USDC, DAI, and USDT, it only accepts ETH-SARCO UNI-V2 LP tokens. It would run for one year and would distribute the tokens linearly. 


---