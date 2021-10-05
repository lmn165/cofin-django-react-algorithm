import React from "react";
import styled from "styled-components";

const Linear = () => (
    <>
        <h1>Linear 페이지 입니다.</h1>
        <MenuTable>
        <MenuTr>
            <LinkTd></LinkTd>
            <ContentTd rowSpan="25"></ContentTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        <MenuTr>
            <LinkTd></LinkTd>
        </MenuTr>
        </MenuTable>
    </>
)

export default Linear

const MenuTable = styled.table`
    border: 1px solid black;
`
const MenuTr = styled.tr`
    height: 50px;
`

const LinkTd = styled.td` 
    width: 250px;
    border: 1px solid black;
`
const ContentTd = styled.td`
    width: 500px;
`