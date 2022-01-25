--TEST--
IntlCalendar::inDaylightTime(): bad arguments
--INI--
date.timezone=Atlantic/Azores
--EXTENSIONS--
intl
--FILE--
<?php
ini_set("intl.error_level", E_WARNING);

var_dump(intlcal_in_daylight_time(1));
?>
--EXPECTF--
Fatal error: Uncaught TypeError: intlcal_in_daylight_time(): Argument #1 ($calendar) must be of type IntlCalendar, int given in %s:%d
Stack trace:
#0 %s(%d): intlcal_in_daylight_time(1)
#1 {main}
  thrown in %s on line %d
