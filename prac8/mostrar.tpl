<h1>{{n}}  usuarios:</h1>
<table>
<tr><th>ID</th><th>e-mail</th><th>password</th><th>gender</th><th>country</th><th>zip</th><th>year</th><th>likes</th></tr>
%for row in c:
	<tr>
	
		 <td>{{row["_id"]}}</td>
            <td>{{row["email"]}}</td>
            <td>{{row["password"]}}</td>
            <td>{{row["gender"]}}</td>
            %for clave ,valor in row["address"].iteritems():              
        		<td>{{valor}}</td>          
                          
        	%end
            <td>{{row["year"]}}</td>
            %for col in row["likes"]:
                <td>{{col}},</td>
            %end
	
	</tr>
%end
</table>

