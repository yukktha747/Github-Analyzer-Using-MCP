from fastmcp import FastMCP

from tools.profile import github_profile
from tools.repositories import github_repositories
from tools.languages import github_languages
from tools.analysis import analyze_profile

mcp = FastMCP("GitHub Profile Analyzer")

mcp.tool()(github_profile)
mcp.tool()(github_repositories)
mcp.tool()(github_languages)
mcp.tool()(analyze_profile)

if __name__ == "__main__":
    mcp.run()
