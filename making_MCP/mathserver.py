from mcp.server.fastmcp import FastMCP

mcp = FastMCP("maths")




@mcp.tool()
def add(a:int , b:int) -> int:
    """_summary_
    Add two numbers
    """
    return a+b

@mcp.tool()
def multiply(a:int , b:int) -> int:
    """_summary_
    Multiply two numbers
    """
    return a*b

@mcp.tool()
def substract(a:int , b:int) -> int:
    """_summary_
    Substract two numbers
    """
    return a - b

@mcp.tool()
def divide(a:int , b:int) -> int:
    """_summary_
    Divides two numbers and results quotient
    """
    return a // b

if __name__=="__main__":
    mcp.run(transport="stdio")


 