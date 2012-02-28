##FastLinks
*Missing simple links parser for python & humans*

Use this component if you want to get **http links** from content in a **fast** ( **very** ) way.

###Overview

Imagine you have this html content:
	
	<LINK REL="SHORTCUT ICON" HREF="favicon.ico" />
	
	src='/clickme.php?id=10&amp;stats=23d'

    URL="http://www.testsite.com/verygood.html"

    href='www.testsite.com/hello placentas/word.htm'
    href='../test.html'
    
	
And all you want to do is just get list of normal looking links from it.

###You can do it now!!

just:

	 links = getLinks(content, 'http://www.testsite.com/')

#### Isn't that trolololowesome ?!

output:

	[1] http://www.testsite.com/test.html
	[2] http://www.testsite.com/hello placentas/word.htm
	[3] http://www.testsite.com/favicon.ico
	[4] http://www.testsite.com/verygood.html
	[5] http://www.testsite.com/clickme.php?id=10&stats=23d

### Please feel free to improve it if you like :)

![image](http://img193.imageshack.us/img193/5605/tumblrlznr805hcb1r3zat8.png)


### Also you can try (more power on data mining) [CustomStringParser](https://github.com/dotpot/Custom-String-Parser)
