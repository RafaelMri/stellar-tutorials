title: Technical appendix
date: 2013-07-15 12:00:00
order: 99

# Technical appendix

__Definition (safety)__. A __consensus protocol__ has __safety__ iff it has: 1) __agreement__ (all outputs have the same value), and 2) __validity__ (the output value is one of the nodes')  
__Definition (liveness)__. A __consensus protocol__ has __liveness__ iff it has: __termination__ (every nonfaulty node outputs a value)  
__Definition (fault tolerance)__. A __consensus protocol__ has __fault tolerance__ iff it: 1) can recover from the failure of a node, and 2) has __fail-stop__ (endures node __crashes__), and 3) has __Byzantine fault-tolerance__ (endures node __arbitrary behavior__)  
__Definition (bivalent)__. A __consensus protocol__ is in a __bivalent__ state iff the network can affect which value nodes choose  
__Definition (univalent, `x`-valent)__. A __consensus protocol__ is in a __univalent__ state iff only 1 output value is possible! For a value of `x`, the state is called __`x`-valent__  
__Definition (stuck)__. A __consensus protocol__ is in a __stuck__ state iff some nonfaulty node can never output a value  

__Definition (ill-behaved / well-behaved)__.  
__Definition (befouled / intact)__.  
__Definition (failed / correct)__.  

__Definition (quorum slice)__.  A __quorum slice__ `q` of a node `v` is a set of nodes that is sufficient to influence `v`  
__Definition (FBAS)__.          An __FBAS__ is a pair `(V, Q)`; `V` is a set of __nodes__, `Q` is a function mapping each node `v` is to some nonempty set of __sets of nodes__ `Q[v]`, the set of all quorum slices `q` of `v`  

__Definition (quorum)__.        A __quorum__ is a set of nodes containing a quorum slice of each member  

__Definition (vote)__.          A node    __votes__ for     statement `a` iff  
__Definition (externalize)__.   A node    __externalizes__  statement `a` iff  
__Definition (accept)__.        A node    __accepts__       statement `a` iff  
__Definition (reject)__.        A node    __rejects__       statement `a` iff it __accepts__ statement `NOT a`  
__Definition (ratify)__.        A quorum  __ratifies__      statement `a` iff each of its nodes __votes__ for `a`  s
__Definition (agree)__.         To __agree__ with a statement `a` means  
__Definition (confirm)__.       To __confirm__ statement `a` means to __ratify__ statement `accept[a]`  
__Definition (neutralize)__.  

__Definition (ballot)__.        A __ballot__ is a pair `(n, x)` (`n` is a counter, `x` is a __candidate operation__) satisfying: if `(n, x)` is safe for some `n`, then `x` is safe  
__Definition (commit ballot)__. [...] Equivalently, to commit a ballot is to not abort it  
__Definition (abort ballot)__.  [...] Equivalently, to abort a ballot is to not commit it  
__Definition (prepared)__.      A ballot is __prepared__ iff each incompatible ballot with a lower `n` has been __aborted__  

__Definition (irrefutable)__  
__Definition (neutralizable)__  

The __dsets__ we care about are those that contain all __ill-behaved__ nodes!  
The __dsets__ in an FBAS `(V, Q)` are given a priori by the quorum function!  
Well- and ill-behaved nodes are determined at runtime!  

The set of all ill-behaved nodes is a dset??  
__Theorem__. In an FBAS with quorum intersection, the set of all __befouled__ nodes is a __dset__.  
The set of all failed nodes is a dset??  

__Definition__. A __dset__ is a set of nodes [...] 
__Definition__. A node `v` is __intact__ iff there exists a dset containing all ill-behaved nodes and not containing `v`  
__Definition__. Let `v` be a node. A __`v`-blocking set__ is a set of nodes that intersects every quorum slice of `v`  
__Definition__. A statement is irrefutable is no __intact__ node can vote against it  

__Theorem (FLP impossibility)__. No __asynchronous deterministic consensus protocol__ can have __safety__, __liveness__, and __fault tolerance__  

__Theorem__. The union of two quorums is also a quorum.  
__Theorem__. The intersection of two dsets is also a dset.  
__Theorem__. Two __well-behaved__ nodes (in an FBAS with quorum intersection) cannot __ratify__  contradictory statements.  
__Theorem__. Two __well-behaved__ nodes (in an FBAS with quorum intersection) cannot __confirm__ contradictory statements.  
__Theorem__. Two __intact__       nodes (in an FBAS with quorum intersection) cannot __ratify__  contradictory statements.  
__Theorem__. Two __intact__       nodes (in an FBAS with quorum intersection) cannot __accept__  contradictory statements.  
__Theorem__. Two contradictory statements cannot be ratified in an FBAS with quorum intersection and no ill-behaved nodes.  
__Theorem__. Let `B` be a set of nodes. An FBAS has quorum availability despite `B` iff `B` isn't `v`-blocking for any node `v`.  
__Theorem__. If a node `v` is intact, then no `v`-blocking set contains solely befouled nodes.  

__The Fundamental Theorem of federated Byzantine agreement systems__. If an intact node (in an FBAS with quorum intersection) __confirms__ a statement `a`, then every intact node will eventually confirm `a`.  

-------

<!-- __Consensus__ is the key to __replication__  
The main challenge of __replicating data__: __keeping copies in sync__  
Common technique: organize system as a __replicated state machine__: 1) all replicas agree on the __inital state__ of the system, and 2) all replicas agree on a __sequence of operations__ (needs consensus over _all_ replicas on _each_ operation!)  

A __ledger__ is the __state__ of __all entities at a given time__: accounts (ID/balance), the set of all transactions that will tie this ledger to the next ledger. There's also invariants: all transactions are valid in terms of their __signatures__, balance can't be negative, etc.!  

SCP is the first Byzantine agreement protocol to give each participant maximum freedom in chosing which combinations of other participants to trust.

Like nonfederated Byzantine agreement, FBA addresses the problem of updating replicated state, such as a ledger.

In a consensus protocol, nodes exchange messages __asserting statements__ about __slots__.
We assume such assertions cannot be forged (this can be guaranteed if nodes are named by public key and they digitally sign messages).
When a node hears a __quorum slice__ assert a statement, it assumes __no functioning node will ever contradict that statement__.
To permit progress in the face of node failures, __a node may have multiple slices__, _any one of which is sufficient to convince it of a statement_.
At a high level, then, an FBA system consists of a loose confederation of nodes each of which has chosen one or more slices.

A __quorum__ is a set of nodes sufficient to reach agreement  
A __quorum slice__ is the subset of a quorum convincing one particular node of agreement  
A __quorum slice__ may be smaller than a __quorum__  

To ensure consensus is possible, a protocol must ensure that every statement is __irrefutable__ (so cannot get stuck) or __neutralizable__ (so cannot block progress). There are two popular approaches to crafting neutralizable statements: the __view-based__ approach and the __ballot-based__ approach.

__Ballot-based__ protocols associate the __values__ in votes with strictly increasing __ballot numbers__. If a __ballot__ gets stuck, nodes retry the __same slot__ with a higher ballot, taking care never to select values that would contradict prior stuck ballots.  

__SCP__ consists of 2 protocols:

1. A __nomination protocol__  
2. A __ballot protocol__  

The __nomination protocol__ produces __candidate values__ for a __slot__. Eventually it produces the same set of candidate values at each intact node (but no one knows _when_!)  
The __ballot protocol__ uses __federated voting__ to commit/abort ballots associated with __composite values__  
The __ballot protocol__ is executed when nodes __guess__ that the nomination protocol has __converged__  

SCP can only guarantee __safety__ when nodes choose suitable quorum slices!  
SCP is __optimal__ is __safety__, but NOT in __performance__ or __latency__  
SCP can suffer __perpetual preemption__  
FBA does NOT require continuity of participants over time! If all nodes leave forever, we're boned, but if they leave for a finite amount of time, and then return, then the system continues   -->
