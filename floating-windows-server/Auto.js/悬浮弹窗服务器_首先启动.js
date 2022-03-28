var address=new java.net.InetAddress.getByName("127.0.0.1");
var server=new java.net.ServerSocket(1860,1,address);
var client=server.accept();
toast("Successfully connected to the Python client.");
var in_byte=client.getInputStream();
var in_char=new java.io.InputStreamReader(in_byte,"utf-8");
var buffer=new java.io.BufferedReader(in_char);
var line0,line1;
while(true)
{
    line0=buffer.readLine();
    line1=buffer.readLine();
    if(line0!=null && line1!=null)
    {
        engines.execScript(line0,line1);
    }
}