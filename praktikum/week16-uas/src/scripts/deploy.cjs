const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying EduToken to Sepolia...\n");

  // Get deployer account
  const [deployer] = await hre.ethers.getSigners();
  console.log("📍 Deploying from account:", deployer.address);
  
  const balance = await deployer.getBalance();
  console.log("💰 Account balance:", hre.ethers.utils.formatEther(balance), "ETH\n");

  if (balance.lt(hre.ethers.utils.parseEther("0.01"))) {
    console.log("⚠️  WARNING: Balance might be too low for deployment!");
    console.log("💡 Get Sepolia ETH from: https://sepoliafaucet.com\n");
  }

  // Deploy contract
  console.log("⏳ Deploying EduToken contract...");
  const EduToken = await hre.ethers.getContractFactory("EduToken");
  const eduToken = await EduToken.deploy();
  
  await eduToken.deployed();

  console.log("✅ EduToken deployed successfully!");
  console.log("📝 Contract address:", eduToken.address);
  console.log("👤 Owner address:", deployer.address);
  console.log("🔗 View on Etherscan: https://sepolia.etherscan.io/address/" + eduToken.address);
  
  // Get initial supply
  const totalSupply = await eduToken.totalSupply();
  console.log("💎 Total Supply:", hre.ethers.utils.formatEther(totalSupply), "EDT\n");

  console.log("📋 NEXT STEPS:");
  console.log("1. Copy contract address:", eduToken.address);
  console.log("2. Update contract address in your HTML files:");
  console.log("   - templates/materi.html");
  console.log("   - templates/info_token.html");
  console.log("3. Wait ~1 minute for contract verification");
  console.log("4. Run: python app.py");
  console.log("5. Open: http://127.0.0.1:5000\n");

  // Save deployment info
  const fs = require("fs");
  const deploymentInfo = {
    network: "sepolia",
    contractAddress: eduToken.address,
    ownerAddress: deployer.address,
    deployedAt: new Date().toISOString(),
    explorerUrl: `https://sepolia.etherscan.io/address/${eduToken.address}`
  };
  
  fs.writeFileSync(
    "deployment-info.json",
    JSON.stringify(deploymentInfo, null, 2)
  );
  console.log("💾 Deployment info saved to deployment-info.json");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });