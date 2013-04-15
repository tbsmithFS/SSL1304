<?php

class View {

	function printHeader() {
		header('Content-type: text/html');
	}

	function getView($file = '', $data = '') {

		$fullPath = "/Users/tbsmith/Sites/php.ssl1304.com/views/$file.php";

		if (preg_match("/\w/", $file) && file_exists($fullPath)) {

			include($fullPath);

		}

	}

}

?>




