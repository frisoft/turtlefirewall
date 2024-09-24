#!/usr/bin/perl

#======================================================================
# Turtle Firewall webmin module
#
# Copyright (c) Andrea Frigido
# You may distribute under the terms of either the GNU General Public
# License
#======================================================================


do 'turtlefirewall-lib.pl';
&ReadParse();

$new = $in{'new'};

if( $new ) {
	$heading = "<img src=images/create.png hspace=4>$text{'edit_nat_title_create'}";
	$idx = '';
	$virtual = '';
	$real = '';
	$service = '';
	$port = '';
	$active = 1;
} else {
	$heading = "<img src=images/edit.png hspace=4>$text{'edit_nat_title_edit'}";
	$idx = $in{'idx'};
	%nat = $fw->GetNat($idx);
	$virtual = $nat{'VIRTUAL'};
	$real = $nat{'REAL'};
	$service = $nat{'SERVICE'};
	$port = $nat{'PORT'};
	$active = $nat{'ACTIVE'} ne 'NO';
}
&ui_print_header( $heading, $text{'title'}, "" );

$options_virtual = '';
$options_real = '';
my @options_virtual = ();
my @options_real = ();
@zones = $fw->GetZoneList();
@hosts = $fw->GetHostList();
for my $k (@hosts) {
	my @opt = ( "$k", "$k ($zone{IF})" ); 
	$options_virtual .= '<option'.($k eq $virtual ? ' selected' : '').'>'.$k.'</option>';
	$options_real .= '<option'.($k eq $real ? ' selected' : '').'>'.$k.'</option>';
}

for my $k (@zones) {
	if( $k ne 'FIREWALL' ) {
		my %zone = $fw->GetZone($k);
		# $options_virtual .= '<option'.($k eq $virtual ? ' selected' : '').'>'.$k.' ('.$zone{IF}.')</option>';
		my @opt = ( "$k", "$k ($zone{IF})" ); 
		pusth(@items_virtual, \@opt);
	}
}

print &ui_subheading($heading);
print &ui_form_start("save_nat.cgi", "post");
print &ui_hidden("idx", $idx);

if( !$new ) {
	$col = "<b>$idx</b>";
	print &ui_columns_row([ "<img src=images/hash.png hspace=4><b>ID</b>", $col ], \@tds);
}

$col = &ui_select("virtual", $virtual, \@items_virtual);

print "<br>
	<form action=\"save_nat.cgi\">
	<input type=\"hidden\" name=\"idx\" value=\"$idx\">
	<table border width=\"100%\">
		<tr $tb>
			<th>".($new ? $text{edit_nat_title_create} : $text{edit_nat_title_edit})."</th>
		</tr>
		<tr $cb>
			<td>
			<table width=\"100%\">";
if( ! $new ) { print "
			<tr>
				<td><b>#</b></td>
				<td><b><tt>$idx</tt></b></td>
			</tr>";
}
print "			<tr>
				<td width=\"10%\"><b><nobr>$text{virtual_host}<nobr></b></td>
				<td><select name=\"virtual\">$options_virtual</select></td>
			</tr>
			<tr>
				<td><b>$text{real_host}</b></td>
				<td><select name=\"real\">$options_real</select></td>
			</tr>
			<tr>
				<td><b>$text{nat_service}</b></td>
				<td><br>";
				formService( $service, $port, 1 );
print "				<br></td>
			</tr>
			<tr>
				<td><b>$text{nat_active}</b></td>
				<td><input type=\"checkbox\" name=\"active\" value=\"1\"".($active ? ' checked' : '')."></td>
			</tr>
			</table>
			</td>
		</tr>
	</table>";

print "<table width=\"100%\"><tr>";
if( $new ) {
	print '<td><input type="submit" name="new" value="'.$text{button_create}.'"></td>';
} else {
	print '<td><input type="submit" name="save" value="'.$text{button_save}.'"></td>';
	print '<td align="right"><input type="submit" name="delete" value="'.$text{button_delete}.'"></td>';
}
print "</tr></table>";
print "</form>";

print "<br><br>";
&ui_print_footer('list_items.cgi','items list');
