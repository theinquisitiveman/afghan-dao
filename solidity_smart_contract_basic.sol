// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PdfStorage {
    mapping(uint => string) public pdfData;

    function storePdf(uint pageNum, string memory hexString) public {
        pdfData[pageNum] = hexString;
    }

    function getPdf(uint pageNum) public view returns (string memory) {
        return pdfData[pageNum];
    }
}
