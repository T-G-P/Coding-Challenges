<?php
/* Enter your code here. Read input from STDIN. Print output to STDOUT */

$stdin = file_get_contents('php://stdin', 'r');
$result = preg_replace("/^\\s+/m", "", $stdin);

preg_match_all("/(?<!\"|\')(?:\/\/)[^\r\n]*|\/\*[\s\S]*?\*\//", $result, $matches);
foreach ($matches[0] as $value) {
    echo $value."\n";
}

?>
