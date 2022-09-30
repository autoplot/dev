package testjavaparser;

import japa.parser.JavaParser;
import japa.parser.ParseException;
import japa.parser.ast.Node;
import japa.parser.ast.expr.AssignExpr;
import japa.parser.ast.expr.BinaryExpr;
import japa.parser.ast.expr.Expression;
import japa.parser.ast.expr.IntegerLiteralExpr;
import japa.parser.ast.expr.NameExpr;
import japa.parser.ast.stmt.Statement;

/**
 *
 * @author jbf
 */
public class TestJavaParser {

    public static String repr( Node n ) {
        switch ( n.getClass().getSimpleName() ) {
            case "foo":
                return "foo";
            case "AssignExpr":
                return ((AssignExpr)n).getOperator().toString();
            case "BinaryExpr":
                return ((BinaryExpr)n).getOperator().toString();
            case "NameExpr":
                return ((NameExpr)n).getName();
            case "IntegerLiteralExpr":
                return ((IntegerLiteralExpr)n).getValue();
            default:
                return n.getClass().getSimpleName();
        }
    }
    public static void printNode( String indent, Node n ) {
        System.out.print(indent);
        String s= repr(n);
        int i= s.indexOf("\n");
        if (i>-1) s= s.substring(0,Math.min(20,i) );
        System.out.print(s);
        System.out.print(" ");
        System.out.println(n.getClass().getName());
        String childIndent = indent+"   ";
        n.getChildrenNodes().forEach((nchild) -> {
            printNode( childIndent, nchild );
        });
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ParseException {
        Expression parseExpression = japa.parser.JavaParser.parseExpression("3+5*6");
        printNode( "", parseExpression );
        
        Statement statement;
        
        String scode;
        scode= "switch ( ch ) {\n" +
"                            case '{': if ( !inQuote ) braceLevel++; break;\n" +
"                            case '}': if ( !inQuote ) braceLevel--; break;\n" +
"                     def       case '\"': inQuote= !inQuote; break;\n" +
"                            case '\\\\': backSlash= true; break;\n" +
"                            default:\n" +
"                        }";
        //statement= JavaParser.parseStatement(scode); 
        //printNode( "", statement );
        
        statement=  JavaParser.parseStatement( "x=3+5*6;" );
        printNode( "", statement );
    }
    
}
