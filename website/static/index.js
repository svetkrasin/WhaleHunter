function deleteWallet(walletId) {
	fetch("/delete-wallet", {
		method: "POST",
		body: JSON.stringify({ walletId: walletId }),
	}).then((_res) => {
		window.location.href = "/";
	});
}