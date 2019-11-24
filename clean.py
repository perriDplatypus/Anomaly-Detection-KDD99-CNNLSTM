import pandas as pd

col_names = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes',
             'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
             'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
             'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
             'num_access_files', 'num_outbound_cmds', 'is_host_login',
             'is_guest_login', 'count', 'srv_count', 'serror_rate',
             'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
             'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
             'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
             'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
             'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
             'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
             'dst_host_srv_rerror_rate']
data = pd.read_csv('D:/Major Project/Datasets/unlabeled.csv',
                   header=None, names=col_names)
df = data.dropna()
df['protocol_type'] = df['protocol_type'].replace('udp', '0')
df['protocol_type'] = df['protocol_type'].replace('tcp', '1')
df['protocol_type'] = df['protocol_type'].replace('icmp', '2')
df['service'] = df['service'].replace('private', '0')
df['service'] = df['service'].replace('domain_u', '1')
df['service'] = df['service'].replace('http', '2')
df['service'] = df['service'].replace('smtp', '3')
df['service'] = df['service'].replace('ftp_data', '4')
df['service'] = df['service'].replace('ftp', '5')
df['service'] = df['service'].replace('eco_i', '6')
df['service'] = df['service'].replace('other', '7')
df['service'] = df['service'].replace('auth', '8')
df['service'] = df['service'].replace('ecr_i', '9')
df['service'] = df['service'].replace('IRC', '10')
df['service'] = df['service'].replace('X11', '11')
df['service'] = df['service'].replace('finger', '12')
df['service'] = df['service'].replace('time', '13')
df['service'] = df['service'].replace('domain', '14')
df['service'] = df['service'].replace('telnet', '15')
df['service'] = df['service'].replace('pop_3', '16')
df['service'] = df['service'].replace('ldap', '17')
df['service'] = df['service'].replace('login', '18')
df['service'] = df['service'].replace('name', '19')
df['service'] = df['service'].replace('ntp_u', '20')
df['service'] = df['service'].replace('http_443', '21')
df['service'] = df['service'].replace('sunrpc', '22')
df['service'] = df['service'].replace('printer', '23')
df['service'] = df['service'].replace('systat', '24')
df['service'] = df['service'].replace('tim_i', '25')
df['service'] = df['service'].replace('netstat', '26')
df['service'] = df['service'].replace('remote_job', '27')
df['service'] = df['service'].replace('link', '28')
df['service'] = df['service'].replace('urp_i', '29')
df['service'] = df['service'].replace('sql_net', '30')
df['service'] = df['service'].replace('bgp', '31')
df['service'] = df['service'].replace('pop_2', '32')
df['service'] = df['service'].replace('tftp_u', '33')
df['service'] = df['service'].replace('uucp', '34')
df['service'] = df['service'].replace('imap4', '35')
df['service'] = df['service'].replace('pm_dump', '36')
df['service'] = df['service'].replace('nnsp', '37')
df['service'] = df['service'].replace('courier', '38')
df['service'] = df['service'].replace('daytime', '39')
df['service'] = df['service'].replace('iso_tsap', '40')
df['service'] = df['service'].replace('echo', '41')
df['service'] = df['service'].replace('discard', '42')
df['service'] = df['service'].replace('ssh', '43')
df['service'] = df['service'].replace('whois', '44')
df['service'] = df['service'].replace('mtp', '45')
df['service'] = df['service'].replace('gopher', '46')
df['service'] = df['service'].replace('rje', '47')
df['service'] = df['service'].replace('ctf', '48')
df['service'] = df['service'].replace('supdup', '49')
df['service'] = df['service'].replace('hostnames', '50')
df['service'] = df['service'].replace('csnet_ns', '51')
df['service'] = df['service'].replace('uucp_path', '52')
df['service'] = df['service'].replace('nntp', '53')
df['service'] = df['service'].replace('netbios_ns', '54')
df['service'] = df['service'].replace('netbios_dgm', '55')
df['service'] = df['service'].replace('netbios_ssn', '56')
df['service'] = df['service'].replace('vmnet', '57')
df['service'] = df['service'].replace('Z39_50', '58')
df['service'] = df['service'].replace('exec', '59')
df['service'] = df['service'].replace('shell', '60')
df['service'] = df['service'].replace('efs', '61')
df['service'] = df['service'].replace('klogin', '62')
df['service'] = df['service'].replace('kshell', '63')
df['service'] = df['service'].replace('icmp', '64')
df = df[df.service != 'harvest']
df = df[df.service != 'http_2784']
df = df[df.service != 'http_8001']
df = df[df.service != 'urh_i']
df = df[df.service != 'aol']
df['flag'] = df['flag'].replace('SF', '0')
df['flag'] = df['flag'].replace('SH', '1')
df['flag'] = df['flag'].replace('RSTR', '2')
df['flag'] = df['flag'].replace('REJ', '3')
df['flag'] = df['flag'].replace('S0', '4')
df['flag'] = df['flag'].replace('S1', '5')
df['flag'] = df['flag'].replace('S2', '6')
df['flag'] = df['flag'].replace('S3', '7')
df['flag'] = df['flag'].replace('RSTO', '8')
df['flag'] = df['flag'].replace('RSTOS0', '9')
df['flag'] = df['flag'].replace('OTH', '10')
df["protocol_type"] = pd.to_numeric(df["protocol_type"])
df["service"] = pd.to_numeric(df["service"])
df["flag"] = pd.to_numeric(df["flag"])
df.to_csv("D:/Major Project/Datasets/data.csv", index=False)
