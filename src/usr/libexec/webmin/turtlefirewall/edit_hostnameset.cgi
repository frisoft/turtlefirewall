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
$hostnameset = $in{'hostnameset'};
$newhostnameset = $in{'newhostnameset'};

if( $new ) {
	&ui_print_header( "<img src=images/hostnameset.png hspace=4>$text{'edit_hostnameset_title_create'}", $text{'title'}, "" );
} else {
	&ui_print_header( "<img src=images/hostnameset.png hspace=4>$text{'edit_hostnameset_title_edit'}", $text{'title'}, "" );
}

my %h = $fw->GetHostNameSet($hostnameset);
my $hostnames = $h{'HOSTNAMES'};
my $description = $h{'DESCRIPTION'};

my @hostnamesetlist = split(/,/, $hostnames);

print "<br><br>
	<form action=\"save_hostnameset.cgi\">
	<table border width=\"100%\">
		<tr $tb>
			<th>".($new ? $text{'edit_hostnameset_title_create'} : $text{'edit_hostnameset_title_edit'})."</th>
		</tr>
		<tr $cb>
			<td>
			<table width=\"100%\"><tr>
				<td style=vertical-align:top><img src=images/hostnameset.png hspace=4><b>$text{'name'}</b></td>
			<td style=vertical-align:top>";
if( $new ) {
	print "		<input type=\"text\" name=\"hostnameset\">";
} else {
	print '		<input type="text" name="newhostnameset" value="'.$hostnameset.'">';
	print '		<input type="hidden" name="hostnameset" value="'.$hostnameset.'">';
}
print			'</td></tr>
			<tr>
				<td style=vertical-align:top><img src=images/hostname.png hspace=4><b>'.$text{'hostnames'}.'</b></td>
				<td style=vertical-align:top>
			<table width="100%">
                   	<tr><td>';
print	    		  &ui_textarea("hostnamesetlist", join("\n", @hostnamesetlist), 10, 20);
print			'</td></tr>
			</table>
			</td></tr>';

print 			'<tr><td style=vertical-align:top><img src=images/info.png hspace=4><b>'.$text{'description'}.'</b></td>';
print			'<td style=vertical-align:top><input type="text" name="description" size="60" value="'.$description.'"></td>';
print			'</tr>';

print			'</table>
			</td>
		</tr>
	</table>';

print "<table width=\"100%\"><tr>";
if( $new ) {
        print '<td>'.&ui_submit( $text{'button_create'}, "new").'</td>';
} else {
        print '<td>'.&ui_submit( $text{'button_save'}, "save").'</td>';
        print '<td style=text-align:right>'.&ui_submit( $text{'button_delete'}, "delete").'</td>';
}
print "</tr></table>";
print "</form>";

print "<br><br>";
&ui_print_footer('list_items.cgi','items list');
