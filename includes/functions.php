<?php
// This file is the place to store all basic functions

function mysql_prep( $value ) { // This function cleans text entered by users for stroage in the database
	$magic_quotes_active = get_magic_quotes_gpc();
	$new_enough_php = function_exists( "mysql_real_escape_string" ); // i.e. PHP >= v4.3.0
	if( $new_enough_php ) { // PHP v4.3.0 or higher
		// undo any magic quote effects so mysql_real_escape_string can do the work
		if( $magic_quotes_active ) { $value = stripslashes( $value ); }
		$value = mysql_real_escape_string( $value );
	} else { // before PHP v4.3.0
		// if magic quotes aren't already on then add slashes manually
		if( !$magic_quotes_active ) { $value = addslashes( $value ); }
		// if magic quotes are active, then the slashes already exist
	}
	return $value;
}

function nav_bar() { //Displays list of links for site navigation
	echo "<a href=\"index.php\">Home</a><br /> <br />";
	echo "<a href=\"schedule.php\">Calendar of Events</a><br /> <br />";
	echo "<a href=\"projects.php\">Projects</a><br /> <br />";
	echo "<a href=\"constitution.php\">Our Constitution</a><br /> <br />";
	echo "<a href=\"faq.php\">Frequently Asked Questions</a><br /> <br />";
	echo "<a href=\"about.php\">About the Computer Club</a><br /> <br />";
}

?>