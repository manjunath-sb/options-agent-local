from mcp.server import FastMCP

from tools.trend_evaluator import evaluate_trend_strength
from tools.volatility_evaluator import evaluate_volatility_regime
from tools.risk_boundary_evaluator import evaluate_risk_boundaries
from tools.event_risk_evaluator import evaluate_event_risk



def start_mcp_server():
    mcp = FastMCP("Options Analysis MCP Server")

    @mcp.tool(
        name="evaluate_trend_strength",
        description="Evaluate directional trend and confidence based on trend, volume, and market bias"
    )
    def trend_strength_tool():
        return evaluate_trend_strength()

    @mcp.tool(
        name="evaluate_volatility_regime",
        description="Evaluate volatility regime and whether options are cheap or expensive"
    )
    def volatility_regime_tool():
        return evaluate_volatility_regime()

    print("Starting Options MCP Server on http://localhost:8000")
    mcp.run(transport="streamable-http")

    @mcp.tool(
        name="evaluate_risk_boundaries",
        description="Evaluate whether downside and upside risk boundaries are clearly defined"
    )
    def risk_boundary_tool():
        return evaluate_risk_boundaries()
    
    @mcp.tool(
    name="evaluate_event_risk",
    description="Evaluate risk arising from proximity to earnings or other major events"
    )
    def event_risk_tool():
        return evaluate_event_risk()


if __name__ == "__main__":
    start_mcp_server()
