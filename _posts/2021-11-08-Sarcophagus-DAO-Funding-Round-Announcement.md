---
layout: post
author: sarco_builders
title: Sarcophagus DAO Funding Round Annoucement 
---


<img class="post-hero-img img-fluid" src="{{site.baseurl}}/assets/img/sarco_placeholder.png"/>


The Sarcophagus DAO is happy to announce the closing of its $1.8m initial funding round led by [Placeholder Ventures](https://www.placeholder.vc/), with participation from [Greenfield One](https://www.greenfield.one/), [Blockchain.com Ventures](https://www.blockchain.com/ventures), [Coral Defi](https://www.coralcapital.io/), Luis Cuende (Aragon), and Kain Warwick (Synthetix).

This is a major milestone in our efforts as a collective DAO. This funding will supercharge our ability to deliver on the promise of a truly decentralized and robust dead man's switch; something that has never existed in the past. 

One may ask: Why would a decentralized project raise money from VCs when it is mechanically possible to raise money on the open market? There are two reasons: 1. Leadership, 2. Labor. 

### 1. Leadership

Any project of consequence needs leaders, and we think that by working with some of the most experienced and intelligent people in the space, we can vastly improve our chances of success. This is a DAO, there are no dictators, but that does not mean that there are no leaders. Every single investor in the Sarcophagus DAO is well versed in DAO economics and had to interact directly with several on-chain contracts to complete the placement (more on structure later).

There is plenty of money floating around crypto land right now, but as always there are very few people that truly understand what is happening under the surface. We optimized for expertise and experience, not valuation or round size.

### 2. Labor

A DAO is a collection of people working independently towards a common goal. The more people that are working towards that goal, the better. By bringing on technically savvy investors, we are also bringing on teams that are highly incentivized to help not just fund the project, but to be the first to operate it's core infrastructure.

## Economics

The funding round was completed by using a whitelisted SARCO/USDC swap contract (pioneered by Lido), funded with $SARCO tokens as the result of a DAO vote, and a General Purpose ERC20 linear vesting contract. 

Here's how it works: 

1. The swap contract with whitelisted addresses + allocations is launched and the start function is called: [https://etherscan.io/address/0x08cbe2703b030432bcc6ce5950b465186502e610](https://etherscan.io/address/0x08cbe2703b030432bcc6ce5950b465186502e610)

2. The DAO votes to fund the swap contract with the amount of tokens agreed upon with the investors, the documents and allocations are also linked to the vote via Arweave: [https://client.aragon.org/#/sarcophagus/0xf483c1f7858dd19915d0689d26cb3487fc90b640/vote/5/](https://client.aragon.org/#/sarcophagus/0xf483c1f7858dd19915d0689d26cb3487fc90b640/vote/5/)

3. Once the vote passes, there is a 30 day window where the whitelisted addresses are able to perform the swap. 

4. When each investor performs the swap, their tokens are sent to a general purpose vesting contract [https://etherscan.io/address/0x8727c592f28f10b42eb0914a7f6a5885823794c0](https://etherscan.io/address/0x8727c592f28f10b42eb0914a7f6a5885823794c0) with a two year vesting period. The tokens are unlocked linearly and the investor can claim them whenever they like.

5. If there are any leftover tokens from investors that were whitelisted but failed to make the swap for any reason within the timeframe, those tokens are recovered back into the DAO.

## What We Learned

It's hard to be the first to try something, there is an excise amount of labor and testing that needs to happen. Luckily the field we are working in is the most transparent and helpful in the world. We were able to reach out to other teams who have done similar things and get their advice, we were also lucky enough to be working on a project that investors will do more work than normal to participate in. 

A few things that we will keep in mind for the next funding round: 

- Requiring investors to perform semi-complex on-chain actions is one of the best sorting functions for future partners. If an investor balked at the idea of using a swap contract + DAO vote it was easy to spot the red flag and end discussions. 

- Investors aren't used to all getting the same deal. It took a lot of coordination and waterfall style work to get all of the participants aligned on a single set of documents and economics. 

- Good investors don't care about long lockups, they care about ability to participate in network activities in order to double-down on their thesis.

## What's Next

Building! Lots of improvements coming to the project including L2 support. Please join the [Discord](https://discord.gg/XPNKEZW) and [Telegram](https://t.me/sarcophagusio) channels for announcements about future incentives for both dead man's switch creators (Embalmers) and node operators (Archaeologists) coming shortly. 
