from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.node import OVSKernelSwitch, RemoteController
from time import sleep

from datetime import datetime
from random import randrange, choice

class MyTopo( Topo ):

    def build( self ):
        #cls:class of the switch....By default `UserSwitch`... Open vSwitch (OVS) 
        #يمكن أن يدعم `OVSKernelSwitch` إصدارات OpenFlow حتى 1.5، بينما يدعم `UserSwitch` فقط OpenFlow حتى الإصدار 1.0.

        s1 = self.addSwitch( 's1', cls=OVSKernelSwitch, protocols='OpenFlow13' )
        #مما يعني أن المضيف سيكون لديه حق الوصول إلى 1/20 أو 5% من دورات وحدة المعالجة المركزية المتاحة
        h1 = self.addHost( 'h1', cpu=1.0/20,mac="00:00:00:00:00:01", ip="10.0.0.1/24" )
        h2 = self.addHost( 'h2', cpu=1.0/20, mac="00:00:00:00:00:02", ip="10.0.0.2/24" )
        h3 = self.addHost( 'h3', cpu=1.0/20, mac="00:00:00:00:00:03", ip="10.0.0.3/24" )    

        s2 = self.addSwitch( 's2', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h4 = self.addHost( 'h4', cpu=1.0/20, mac="00:00:00:00:00:04", ip="10.0.0.4/24" )
        h5 = self.addHost( 'h5', cpu=1.0/20, mac="00:00:00:00:00:05", ip="10.0.0.5/24" )
        h6 = self.addHost( 'h6', cpu=1.0/20, mac="00:00:00:00:00:06", ip="10.0.0.6/24" )

        s3 = self.addSwitch( 's3', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h7 = self.addHost( 'h7', cpu=1.0/20, mac="00:00:00:00:00:07", ip="10.0.0.7/24" )
        h8 = self.addHost( 'h8', cpu=1.0/20, mac="00:00:00:00:00:08", ip="10.0.0.8/24" )
        h9 = self.addHost( 'h9', cpu=1.0/20, mac="00:00:00:00:00:09", ip="10.0.0.9/24" )

        s4 = self.addSwitch( 's4', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h10 = self.addHost( 'h10', cpu=1.0/20, mac="00:00:00:00:00:10", ip="10.0.0.10/24" )
        h11 = self.addHost( 'h11', cpu=1.0/20, mac="00:00:00:00:00:11", ip="10.0.0.11/24" )
        h12 = self.addHost( 'h12', cpu=1.0/20, mac="00:00:00:00:00:12", ip="10.0.0.12/24" )

        s5 = self.addSwitch( 's5', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h13 = self.addHost( 'h13', cpu=1.0/20, mac="00:00:00:00:00:13", ip="10.0.0.13/24" )
        h14 = self.addHost( 'h14', cpu=1.0/20, mac="00:00:00:00:00:14", ip="10.0.0.14/24" )
        h15 = self.addHost( 'h15', cpu=1.0/20, mac="00:00:00:00:00:15", ip="10.0.0.15/24" )

        s6 = self.addSwitch( 's6', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h16 = self.addHost( 'h16', cpu=1.0/20, mac="00:00:00:00:00:16", ip="10.0.0.16/24" )
        h17 = self.addHost( 'h17', cpu=1.0/20, mac="00:00:00:00:00:17", ip="10.0.0.17/24" )
        h18 = self.addHost( 'h18', cpu=1.0/20, mac="00:00:00:00:00:18", ip="10.0.0.18/24" )

        # Add links

        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s1 )

        self.addLink( h4, s2 )
        self.addLink( h5, s2 )
        self.addLink( h6, s2 )

        self.addLink( h7, s3 )
        self.addLink( h8, s3 )
        self.addLink( h9, s3 )

        self.addLink( h10, s4 )
        self.addLink( h11, s4 )
        self.addLink( h12, s4 )

        self.addLink( h13, s5 )
        self.addLink( h14, s5 )
        self.addLink( h15, s5 )

        self.addLink( h16, s6 )
        self.addLink( h17, s6 )
        self.addLink( h18, s6 )

        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s4 )
        self.addLink( s4, s5 )
        self.addLink( s5, s6 )

def ip_generator():

    ip = ".".join(["10","0","0",str(randrange(1,19))])#Generating a random number 
    return ip
        
def startNetwork():

    #print "Starting Network"
    topo = MyTopo()
    #net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink, controller=None )
    #net.addController( 'c0', controller=RemoteController, ip='192.168.43.55', port=6653 )

    c0 = RemoteController('c0', ip='192.168.0.101', port=6653)
    #Traffic Control Link&&&`WIFI`
    #يسمح لك بتكوين معلمات الارتباط مثل عرض النطاق الترددي والتأخير والارتعاش وفقدان الحزمة.
    #يعد نوع الارتباط هذا مفيدًا في محاكاة الشبكة لأنه غالبًا ما يسمح لك بتكرار أداء شبكات العالم الحقيقي بشكل أكثر دقة.
    net = Mininet(topo=topo, link=TCLink, controller=c0)

    net.start()
#get لاسترداد المضيفين لتنفيذ اوامر عليهم
    
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')
    
    hosts = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18]    
    print("--------------------------------------------------------------------------------")    
    print("Generating traffic ...")    
    #اي ملفات موجودة في ويب سيرفر صار فيني حملا ب HTTP wget
    #`SimpleHTTPServer` is a Python module that allows you to run a basic HTTP server to serve static files in the specified directory. 
    h1.cmd('cd /home/mininet/webserver')
    h1.cmd('python -m SimpleHTTPServer 80 &')
    #Iperf هي أداة اختبار أداء شبكة
    #يستخدم الخادم بشكل أساسي لمراقبة طلبات الاختبار الواردة
    h1.cmd('iperf -s -p 5050 &')
    h1.cmd('iperf -s -u -p 5051 &')#udp server port
    #h1` acts as a web server and measures the performance of incoming connections using `iperf`.
    sleep(2)
    for h in hosts:
        h.cmd('cd /home/mininet/Downloads')
    #من اجل كل تكرار تتولد عشر عبارات طباعة
    for i in range(10):
        
        print("--------------------------------------------------------------------------------")    
        print("Iteration n {} ...".format(i+1))
        print("--------------------------------------------------------------------------------") 
        #Within each iteration, the script generates ICMP traffic between a randomly selected source (`src`) and a randomly generated destination IP address (`dst`).
        for j in range(10):
            src = choice(hosts)#h17
            dst = ip_generator()#h7
            
            if j <9:
                print("generating ICMP traffic between %s and h%s and TCP/UDP traffic between %s and h1" % (src,((dst.split('.'))[3]),src))
                src.cmd("ping {} -c 50 &".format(dst))#ping h17 h7
                src.cmd("iperf -p 5050 -c 10.0.0.1")#generates TCP and UDP traffic between `src` and a fixed IP address `10.0.0.1`
                src.cmd("iperf -p 5051 -u -c 10.0.0.1")
            else:
                print("generating ICMP traffic between %s and h%s and TCP/UDP traffic between %s and h1" % (src,((dst.split('.'))[3]),src))
                src.cmd("ping {} -c 50".format(dst))
                src.cmd("iperf -p 5050 -c 10.0.0.1")
                src.cmd("iperf -p 5051 -u -c 10.0.0.1")
            
            print("%s Downloading index.html from h1" % src)
            src.cmd("wget http://10.0.0.1/index.html")
            print("%s Downloading test.zip from h1" % src)
            src.cmd("wget http://10.0.0.1/test.zip")
        
        h1.cmd("rm -f *.* /home/mininet/Downloads")#removes any downloaded files from the `Downloads` directory on `h1`
        
    print("--------------------------------------------------------------------------------")  
    
    # CLI(net)
    net.stop()

if __name__ == '__main__':
    
    start = datetime.now()
    
    setLogLevel( 'info' )
    startNetwork()
    
    end = datetime.now()
    
    print(end-start)
    print("the end: {}".format((end - start)))