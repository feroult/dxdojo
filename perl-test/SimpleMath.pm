package SimpleMath;
use strict;
use warnings;
use Data::Dumper;
use Exporter qw(import);
 
our @EXPORT_OK = qw(add multiply arrayExample hashExample);
 
sub add {
  my ($x, $y) = @_;
  return $x + $y;
}
 
sub multiply {
  my ($x, $y) = @_;
  return $x * $y;
}

sub arrayExample{
	my @arr = @_;
	for(@arr){
		print ($_);
	}
	print "\n";
}

sub hashExample {
	my %hash;
	$hash{'1'} = 'Test 1';
	$hash{'2'} = 'Test 2';
	for(keys %hash){
		print "$_ $hash{$_}\n";
	}
}
 
1;