public aspect Aspect{

	after(): !within(Aspect) && get(* *) { System.out.println( "GET" ); }
	after(): !within(Aspect) && set(* *) { System.out.println( "SET" ); }
	after(): !within(Aspect) && call(* *(*)) { System.out.println( "CALL" ); }
	after(): !within(Aspect) && execution(* *(*)) { System.out.println( "EXEC" ); }
}
