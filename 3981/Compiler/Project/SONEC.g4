grammar SONEC;

program: ID+;
ID: [a-zA-Z][a-zA-Z0-9]*;
WS: [ \n\t\r]+ -> skip;

