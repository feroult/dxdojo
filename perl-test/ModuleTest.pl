#!/usr/bin/perl
use strict;
use warnings;
use Test::More;
use SimpleMath qw(add multiply arrayExample hashExample);
 
ok( add(6,7) == 13,                   'add' );
ok( multiply(6,7) == 42,              'multiply' );

arrayExample(1,2,3,4,5,6);

hashExample();

done_testing();


