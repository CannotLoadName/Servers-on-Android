var address=new java.net.InetAddress.getByName("127.0.0.1");
var server=new java.net.ServerSocket(1866,1,address);
var client=server.accept();
toast("Successfully connected to the Python client.");
var in_byte=client.getInputStream();
var in_char=new java.io.InputStreamReader(in_byte,"utf-8");
var buffer=new java.io.BufferedReader(in_char);
var out_str=client.getOutputStream();
var writer=new java.io.PrintWriter(out_str);
var files=JSON.parse(buffer.readLine());
var attr=new android.media.AudioAttributes.Builder();
attr.setUsage(android.media.AudioAttributes.USAGE_MEDIA);
attr.setContentType(android.media.AudioAttributes.CONTENT_TYPE_MUSIC);
var spb=new android.media.SoundPool.Builder();
spb.setMaxStreams(files.length);
spb.setAudioAttributes(attr.build());
var sp=spb.build();
var lib={};
var id;
for(var t=0;t<files.length;t++)
{
    id=sp.load(files[t],1);
    if(id!=0)
    {
        lib[files[t]]=id;
    }
}
var key=Object.keys(lib);
writer.write(JSON.stringify(key)+"\n");
writer.flush();
var line0;
while(true)
{
    line0=buffer.readLine();
    if(key.indexOf(line0)!=-1)
    {
        sp.play(lib[line0],1,1,0,0,1);
    }
}