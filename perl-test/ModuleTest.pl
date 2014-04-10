#!/usr/bin/perl
use strict;
use warnings;
use Test::More;
use SimpleMath qw(add multiply);
 
ok( add(6,7) == 13,                   'add' );
ok( multiply(6,7) == 42,              'multiply' );

done_testing();