DIFS = 34.0
#DIFS = 146.0
SIFS = 16.0
CW_min = 15
T_slot = 9.0
#T_slot = 65.0
T_back_off = (( CW_min )/2.0) * T_slot
T_prop = 2.0
T_delim = 8.0
T_ack_header = 24.0
Nss = 3.0
T_preamble = 32.0 + (Nss*4.0) + 4.0
PHY_header_bytes = 3.0
MAC_header_bytes = 28.0
MPDU_delim_bytes = 4.0
Ack_bytes = 32.0
IP_bytes = 1470.0
#IP_bytes = 1400.0
FCS_bytes = 4.0

def toBps(Mbps): return Mbps*1000000.0
def toMbps(bps): return bps/1000000.0
def toMicrosecond(second): return second*1000000.0
def toSecond(microsecond): return microsecond/1000000.0

def T_phy_header(basic_rate): return T_preamble + toMicrosecond( (PHY_header_bytes*8.0)/float(basic_rate) )

def T_tx(nFrames, rate):

	delimeter = (T_delim*8.0)
	mac_header = (MAC_header_bytes*8.0)
	fcs = (FCS_bytes*8.0)
	payload = (IP_bytes*8.0)

	return nFrames * toMicrosecond( (delimeter+mac_header+fcs+payload)/float(rate) )

def T_B_ack(rate): return toMicrosecond( (Ack_bytes*8)/float(rate) ) + T_ack_header

def T_total(nFrames, rate, basic_rate):
	return toSecond( DIFS + T_back_off + T_phy_header(toBps(basic_rate)) + T_tx(nFrames, toBps(rate)) + T_prop + SIFS + T_B_ack(toBps(rate)) + T_prop )
