
<div class="wrapperStyle">
    <h1>cl1p.net - The Internet Clipboard</h1>
    <h2>Copy and paste using the internet</h2>
    <div class="line"></div>

   cl1p.net lets you move information between computers using your brain.

Think up a unique URL that starts this cl1p.net
Example: cl1p.net/xzsygskfwb.
Enter the URL in a browser and type or paste in what you want.
On another computer or smartphone enter in the same URL to retrive the information.
For security the information in the cl1p url is destroyed as soon as it is read. Anyone visiting the same URL at a later time will not be able to see the message.

cl1p.net is great for cases where you need to move data. (Like the contents of a text file) between devices when e-mail, or shared drives is not pratical.

Perhaps you need to move a log file off a computer you don't trust.

Or you might need to move some clipboard info between two seperate computers.

cl1p.net is a very quick and convient way to move data between devices connected to the internet.

Created and maintained by Rob Mayhew.Use at your own risk.

 <h2>Installation</h2>
    <div class="line"></div>

 Use pip to install cl1p.
 
    pip install cl1p
    
 <h2>Usage</h2>
    <div class="line"></div>
    <h3>Create clip</h3>
    <div class="line"></div> 
    
   Use '-l' flag to provide url for clip. Use '-m' flag to provide message for clip.
    
    cl1p -l newclip -m hii
   Above command will create clip at https:cl1p.net/newclip with content 'hii'
   
   
   You can also use '-d' flag to create clip directly from clipboard
   
    cl1p -l newclip -d
    
  <h3>Get clip</h3>
    <div class="line"></div>
    
   Use '-l' flag to provide url for clip.
   
    clip -l newclip
   Above command will fetch clip present at https:cl1p.net/newclip and show its content on terminal
   
   You can also use '-c' flag t copy clip content to clipboard.(Not tested on linux and Mac)
   
    clip -l newclip -c
    
    
    
    
   
   
   
