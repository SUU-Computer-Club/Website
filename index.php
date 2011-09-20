<?php require_once("includes/functions.php"); ?>
<?php include("includes/header.php"); ?>

<h2></h2>
<div class="page-content"></div>
<center>
	<h2>Welcome to the Computer Club at Southern Utah University!</h2>
	<br /> <br />
	<?php if (time() < strtotime("2011-12-09 00:00 MST")) { ?><h3>We meet every Tuesday at 4:00 PM in ELC 310.</h3><?php } ?>
	<h3>Come see what we are doing this week!</h3>
	<br /> <br />
	<embed type="application/x-shockwave-flash"
		src="https://picasaweb.google.com/s/c/bin/slideshow.swf" width="600"
		height="400"
		flashvars="host=picasaweb.google.com&hl=en_US&feat=flashalbum&RGB=0x000000&feed=https%3A%2F%2Fpicasaweb.google.com%2Fdata%2Ffeed%2Fapi%2Fuser%2F116546428115778334917%3Falt%3Drss%26kind%3Dphoto%26access%3Dpublic%26psc%3DF%26q%26uname%3D116546428115778334917"
		pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>
</center>

<?php include("includes/footer.php"); ?>
