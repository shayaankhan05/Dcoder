<!DOCTYPE html>
<!-- saved from url=(0071)https://code.dcoder.tech/question/5b5ee71361601549b1d0b92b?lang=python3 -->
<html lang=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          
          <meta name="mobile-web-app-capable" content="yes">
          <meta name="apple-mobile-web-app-capable" content="yes">
          <meta name="theme-color" content="#536878">
          <title>Happy String</title>
          
          
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="./Happy String_files/css">
          <link rel="stylesheet" href="./Happy String_files/icon">
          <link rel="stylesheet" href="./Happy String_files/all.css" integrity="sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt" crossorigin="anonymous" async="">
          <link rel="manifest" href="https://code.dcoder.tech/manifest.json">
          <link rel="icon" href="https://code.dcoder.tech/question/images/logoIcon.png">
          <link rel="stylesheet" href="./Happy String_files/bundle.33e02623.css">
          <style id="jss-ssr">.MuiPaper-root {
  color: #fff;
  transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  background-color: #424242;
}
.MuiPaper-rounded {
  border-radius: 4px;
}
.MuiPaper-outlined {
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.MuiPaper-elevation0 {
  box-shadow: none;
}
.MuiPaper-elevation1 {
  box-shadow: 0px 2px 1px -1px rgba(0,0,0,0.2),0px 1px 1px 0px rgba(0,0,0,0.14),0px 1px 3px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation2 {
  box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation3 {
  box-shadow: 0px 3px 3px -2px rgba(0,0,0,0.2),0px 3px 4px 0px rgba(0,0,0,0.14),0px 1px 8px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation4 {
  box-shadow: 0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation5 {
  box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 5px 8px 0px rgba(0,0,0,0.14),0px 1px 14px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation6 {
  box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation7 {
  box-shadow: 0px 4px 5px -2px rgba(0,0,0,0.2),0px 7px 10px 1px rgba(0,0,0,0.14),0px 2px 16px 1px rgba(0,0,0,0.12);
}
.MuiPaper-elevation8 {
  box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);
}
.MuiPaper-elevation9 {
  box-shadow: 0px 5px 6px -3px rgba(0,0,0,0.2),0px 9px 12px 1px rgba(0,0,0,0.14),0px 3px 16px 2px rgba(0,0,0,0.12);
}
.MuiPaper-elevation10 {
  box-shadow: 0px 6px 6px -3px rgba(0,0,0,0.2),0px 10px 14px 1px rgba(0,0,0,0.14),0px 4px 18px 3px rgba(0,0,0,0.12);
}
.MuiPaper-elevation11 {
  box-shadow: 0px 6px 7px -4px rgba(0,0,0,0.2),0px 11px 15px 1px rgba(0,0,0,0.14),0px 4px 20px 3px rgba(0,0,0,0.12);
}
.MuiPaper-elevation12 {
  box-shadow: 0px 7px 8px -4px rgba(0,0,0,0.2),0px 12px 17px 2px rgba(0,0,0,0.14),0px 5px 22px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation13 {
  box-shadow: 0px 7px 8px -4px rgba(0,0,0,0.2),0px 13px 19px 2px rgba(0,0,0,0.14),0px 5px 24px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation14 {
  box-shadow: 0px 7px 9px -4px rgba(0,0,0,0.2),0px 14px 21px 2px rgba(0,0,0,0.14),0px 5px 26px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation15 {
  box-shadow: 0px 8px 9px -5px rgba(0,0,0,0.2),0px 15px 22px 2px rgba(0,0,0,0.14),0px 6px 28px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation16 {
  box-shadow: 0px 8px 10px -5px rgba(0,0,0,0.2),0px 16px 24px 2px rgba(0,0,0,0.14),0px 6px 30px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation17 {
  box-shadow: 0px 8px 11px -5px rgba(0,0,0,0.2),0px 17px 26px 2px rgba(0,0,0,0.14),0px 6px 32px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation18 {
  box-shadow: 0px 9px 11px -5px rgba(0,0,0,0.2),0px 18px 28px 2px rgba(0,0,0,0.14),0px 7px 34px 6px rgba(0,0,0,0.12);
}
.MuiPaper-elevation19 {
  box-shadow: 0px 9px 12px -6px rgba(0,0,0,0.2),0px 19px 29px 2px rgba(0,0,0,0.14),0px 7px 36px 6px rgba(0,0,0,0.12);
}
.MuiPaper-elevation20 {
  box-shadow: 0px 10px 13px -6px rgba(0,0,0,0.2),0px 20px 31px 3px rgba(0,0,0,0.14),0px 8px 38px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation21 {
  box-shadow: 0px 10px 13px -6px rgba(0,0,0,0.2),0px 21px 33px 3px rgba(0,0,0,0.14),0px 8px 40px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation22 {
  box-shadow: 0px 10px 14px -6px rgba(0,0,0,0.2),0px 22px 35px 3px rgba(0,0,0,0.14),0px 8px 42px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation23 {
  box-shadow: 0px 11px 14px -7px rgba(0,0,0,0.2),0px 23px 36px 3px rgba(0,0,0,0.14),0px 9px 44px 8px rgba(0,0,0,0.12);
}
.MuiPaper-elevation24 {
  box-shadow: 0px 11px 15px -7px rgba(0,0,0,0.2),0px 24px 38px 3px rgba(0,0,0,0.14),0px 9px 46px 8px rgba(0,0,0,0.12);
}
.MuiSvgIcon-root {
  fill: currentColor;
  width: 1em;
  height: 1em;
  display: inline-block;
  font-size: 1.5rem;
  transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  flex-shrink: 0;
  user-select: none;
}
.MuiSvgIcon-colorPrimary {
  color: #3f51b5;
}
.MuiSvgIcon-colorSecondary {
  color: #00BFA5;
}
.MuiSvgIcon-colorAction {
  color: #fff;
}
.MuiSvgIcon-colorError {
  color: #f44336;
}
.MuiSvgIcon-colorDisabled {
  color: rgba(255, 255, 255, 0.3);
}
.MuiSvgIcon-fontSizeInherit {
  font-size: inherit;
}
.MuiSvgIcon-fontSizeSmall {
  font-size: 1.25rem;
}
.MuiSvgIcon-fontSizeLarge {
  font-size: 2.1875rem;
}
.MuiButtonBase-root {
  color: inherit;
  border: 0;
  cursor: pointer;
  margin: 0;
  display: inline-flex;
  outline: 0;
  padding: 0;
  position: relative;
  align-items: center;
  user-select: none;
  border-radius: 0;
  vertical-align: middle;
  -moz-appearance: none;
  justify-content: center;
  text-decoration: none;
  background-color: transparent;
  -webkit-appearance: none;
  -webkit-tap-highlight-color: transparent;
}
.MuiButtonBase-root::-moz-focus-inner {
  border-style: none;
}
.MuiButtonBase-root.Mui-disabled {
  cursor: default;
  pointer-events: none;
}
.MuiButton-root {
  color: #fff;
  padding: 6px 16px;
  font-size: 0.875rem;
  min-width: 64px;
  box-sizing: border-box;
  transition: background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  line-height: 1.75;
  border-radius: 4px;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
}
.MuiButton-root:hover {
  text-decoration: none;
  background-color: rgba(255, 255, 255, 0.1);
}
.MuiButton-root.Mui-disabled {
  color: rgba(255, 255, 255, 0.3);
}
@media (hover: none) {
  .MuiButton-root:hover {
    background-color: transparent;
  }
}
  .MuiButton-root:hover.Mui-disabled {
    background-color: transparent;
  }
  .MuiButton-label {
    width: 100%;
    display: inherit;
    align-items: inherit;
    justify-content: inherit;
  }
  .MuiButton-text {
    padding: 6px 8px;
  }
  .MuiButton-textPrimary {
    color: #3f51b5;
  }
  .MuiButton-textPrimary:hover {
    background-color: rgba(63, 81, 181, 0.1);
  }
@media (hover: none) {
  .MuiButton-textPrimary:hover {
    background-color: transparent;
  }
}
  .MuiButton-textSecondary {
    color: #00BFA5;
  }
  .MuiButton-textSecondary:hover {
    background-color: rgba(0, 191, 165, 0.1);
  }
@media (hover: none) {
  .MuiButton-textSecondary:hover {
    background-color: transparent;
  }
}
  .MuiButton-outlined {
    border: 1px solid rgba(255, 255, 255, 0.23);
    padding: 5px 15px;
  }
  .MuiButton-outlined.Mui-disabled {
    border: 1px solid rgba(255, 255, 255, 0.3);
  }
  .MuiButton-outlinedPrimary {
    color: #3f51b5;
    border: 1px solid rgba(63, 81, 181, 0.5);
  }
  .MuiButton-outlinedPrimary:hover {
    border: 1px solid #3f51b5;
    background-color: rgba(63, 81, 181, 0.1);
  }
@media (hover: none) {
  .MuiButton-outlinedPrimary:hover {
    background-color: transparent;
  }
}
  .MuiButton-outlinedSecondary {
    color: #00BFA5;
    border: 1px solid rgba(0, 191, 165, 0.5);
  }
  .MuiButton-outlinedSecondary:hover {
    border: 1px solid #00BFA5;
    background-color: rgba(0, 191, 165, 0.1);
  }
  .MuiButton-outlinedSecondary.Mui-disabled {
    border: 1px solid rgba(255, 255, 255, 0.3);
  }
@media (hover: none) {
  .MuiButton-outlinedSecondary:hover {
    background-color: transparent;
  }
}
  .MuiButton-contained {
    color: rgba(0, 0, 0, 0.87);
    box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);
    background-color: #e0e0e0;
  }
  .MuiButton-contained:hover {
    box-shadow: 0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);
    background-color: #d5d5d5;
  }
  .MuiButton-contained.Mui-focusVisible {
    box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);
  }
  .MuiButton-contained:active {
    box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);
  }
  .MuiButton-contained.Mui-disabled {
    color: rgba(255, 255, 255, 0.3);
    box-shadow: none;
    background-color: rgba(255, 255, 255, 0.12);
  }
@media (hover: none) {
  .MuiButton-contained:hover {
    box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);
    background-color: #e0e0e0;
  }
}
  .MuiButton-contained:hover.Mui-disabled {
    background-color: rgba(255, 255, 255, 0.12);
  }
  .MuiButton-containedPrimary {
    color: #fff;
    background-color: #3f51b5;
  }
  .MuiButton-containedPrimary:hover {
    background-color: #303f9f;
  }
@media (hover: none) {
  .MuiButton-containedPrimary:hover {
    background-color: #3f51b5;
  }
}
  .MuiButton-containedSecondary {
    color: #ffcc00;
    background-color: #00BFA5;
  }
  .MuiButton-containedSecondary:hover {
    background-color: rgb(0, 133, 115);
  }
@media (hover: none) {
  .MuiButton-containedSecondary:hover {
    background-color: #00BFA5;
  }
}
  .MuiButton-disableElevation {
    box-shadow: none;
  }
  .MuiButton-disableElevation:hover {
    box-shadow: none;
  }
  .MuiButton-disableElevation.Mui-focusVisible {
    box-shadow: none;
  }
  .MuiButton-disableElevation:active {
    box-shadow: none;
  }
  .MuiButton-disableElevation.Mui-disabled {
    box-shadow: none;
  }
  .MuiButton-colorInherit {
    color: inherit;
    border-color: currentColor;
  }
  .MuiButton-textSizeSmall {
    padding: 4px 5px;
    font-size: 0.8125rem;
  }
  .MuiButton-textSizeLarge {
    padding: 8px 11px;
    font-size: 0.9375rem;
  }
  .MuiButton-outlinedSizeSmall {
    padding: 3px 9px;
    font-size: 0.8125rem;
  }
  .MuiButton-outlinedSizeLarge {
    padding: 7px 21px;
    font-size: 0.9375rem;
  }
  .MuiButton-containedSizeSmall {
    padding: 4px 10px;
    font-size: 0.8125rem;
  }
  .MuiButton-containedSizeLarge {
    padding: 8px 22px;
    font-size: 0.9375rem;
  }
  .MuiButton-fullWidth {
    width: 100%;
  }
  .MuiButton-startIcon {
    display: inherit;
    margin-left: -4px;
    margin-right: 8px;
  }
  .MuiButton-startIcon.MuiButton-iconSizeSmall {
    margin-left: -2px;
  }
  .MuiButton-endIcon {
    display: inherit;
    margin-left: 8px;
    margin-right: -4px;
  }
  .MuiButton-endIcon.MuiButton-iconSizeSmall {
    margin-right: -2px;
  }
  .MuiButton-iconSizeSmall > *:first-child {
    font-size: 18px;
  }
  .MuiButton-iconSizeMedium > *:first-child {
    font-size: 20px;
  }
  .MuiButton-iconSizeLarge > *:first-child {
    font-size: 22px;
  }
  .MuiIconButton-root {
    flex: 0 0 auto;
    color: #fff;
    padding: 12px;
    overflow: visible;
    font-size: 1.5rem;
    text-align: center;
    transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
    border-radius: 50%;
  }
  .MuiIconButton-root:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
  .MuiIconButton-root.Mui-disabled {
    color: rgba(255, 255, 255, 0.3);
    background-color: transparent;
  }
@media (hover: none) {
  .MuiIconButton-root:hover {
    background-color: transparent;
  }
}
  .MuiIconButton-edgeStart {
    margin-left: -12px;
  }
  .MuiIconButton-sizeSmall.MuiIconButton-edgeStart {
    margin-left: -3px;
  }
  .MuiIconButton-edgeEnd {
    margin-right: -12px;
  }
  .MuiIconButton-sizeSmall.MuiIconButton-edgeEnd {
    margin-right: -3px;
  }
  .MuiIconButton-colorInherit {
    color: inherit;
  }
  .MuiIconButton-colorPrimary {
    color: #3f51b5;
  }
  .MuiIconButton-colorPrimary:hover {
    background-color: rgba(63, 81, 181, 0.1);
  }
@media (hover: none) {
  .MuiIconButton-colorPrimary:hover {
    background-color: transparent;
  }
}
  .MuiIconButton-colorSecondary {
    color: #00BFA5;
  }
  .MuiIconButton-colorSecondary:hover {
    background-color: rgba(0, 191, 165, 0.1);
  }
@media (hover: none) {
  .MuiIconButton-colorSecondary:hover {
    background-color: transparent;
  }
}
  .MuiIconButton-sizeSmall {
    padding: 3px;
    font-size: 1.125rem;
  }
  .MuiIconButton-label {
    width: 100%;
    display: flex;
    align-items: inherit;
    justify-content: inherit;
  }
html {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
*, *::before, *::after {
  box-sizing: inherit;
}
strong, b {
  font-weight: bolder;
}
body {
  color: #fff;
  margin: 0;
  font-size: 0.875rem;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  line-height: 1.43;
  letter-spacing: 0.01071em;
  background-color: rgb(17, 17, 17);
}
@media print {
  body {
    background-color: #fff;
  }
}
body::backdrop {
  background-color: rgb(17, 17, 17);
}
@media print {
  .MuiDialog-root {
    position: absolute !important;
  }
}
  .MuiDialog-scrollPaper {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .MuiDialog-scrollBody {
    overflow-x: hidden;
    overflow-y: auto;
    text-align: center;
  }
  .MuiDialog-scrollBody:after {
    width: 0;
    height: 100%;
    content: "";
    display: inline-block;
    vertical-align: middle;
  }
  .MuiDialog-container {
    height: 100%;
    outline: 0;
  }
@media print {
  .MuiDialog-container {
    height: auto;
  }
}
  .MuiDialog-paper {
    margin: 32px;
    position: relative;
    overflow-y: auto;
  }
@media print {
  .MuiDialog-paper {
    box-shadow: none;
    overflow-y: visible;
  }
}
  .MuiDialog-paperScrollPaper {
    display: flex;
    max-height: calc(100% - 64px);
    flex-direction: column;
  }
  .MuiDialog-paperScrollBody {
    display: inline-block;
    text-align: left;
    vertical-align: middle;
  }
  .MuiDialog-paperWidthFalse {
    max-width: calc(100% - 64px);
  }
  .MuiDialog-paperWidthXs {
    max-width: 444px;
  }
@media (max-width:507.95px) {
  .MuiDialog-paperWidthXs.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
  .MuiDialog-paperWidthSm {
    max-width: 600px;
  }
@media (max-width:663.95px) {
  .MuiDialog-paperWidthSm.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
  .MuiDialog-paperWidthMd {
    max-width: 960px;
  }
@media (max-width:1023.95px) {
  .MuiDialog-paperWidthMd.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
  .MuiDialog-paperWidthLg {
    max-width: 1280px;
  }
@media (max-width:1343.95px) {
  .MuiDialog-paperWidthLg.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
  .MuiDialog-paperWidthXl {
    max-width: 1920px;
  }
@media (max-width:1983.95px) {
  .MuiDialog-paperWidthXl.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
  .MuiDialog-paperFullWidth {
    width: calc(100% - 64px);
  }
  .MuiDialog-paperFullScreen {
    width: 100%;
    height: 100%;
    margin: 0;
    max-width: 100%;
    max-height: none;
    border-radius: 0;
  }
  .MuiDialog-paperFullScreen.MuiDialog-paperScrollBody {
    margin: 0;
    max-width: 100%;
  }
  .MuiDrawer-docked {
    flex: 0 0 auto;
  }
  .MuiDrawer-paper {
    top: 0;
    flex: 1 0 auto;
    height: 100%;
    display: flex;
    outline: 0;
    z-index: 1200;
    position: fixed;
    overflow-y: auto;
    flex-direction: column;
    -webkit-overflow-scrolling: touch;
  }
  .MuiDrawer-paperAnchorLeft {
    left: 0;
    right: auto;
  }
  .MuiDrawer-paperAnchorRight {
    left: auto;
    right: 0;
  }
  .MuiDrawer-paperAnchorTop {
    top: 0;
    left: 0;
    right: 0;
    bottom: auto;
    height: auto;
    max-height: 100%;
  }
  .MuiDrawer-paperAnchorBottom {
    top: auto;
    left: 0;
    right: 0;
    bottom: 0;
    height: auto;
    max-height: 100%;
  }
  .MuiDrawer-paperAnchorDockedLeft {
    border-right: 1px solid rgba(255, 255, 255, 0.12);
  }
  .MuiDrawer-paperAnchorDockedTop {
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  }
  .MuiDrawer-paperAnchorDockedRight {
    border-left: 1px solid rgba(255, 255, 255, 0.12);
  }
  .MuiDrawer-paperAnchorDockedBottom {
    border-top: 1px solid rgba(255, 255, 255, 0.12);
  }
  .MuiGrid-container {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    box-sizing: border-box;
  }
  .MuiGrid-item {
    margin: 0;
    box-sizing: border-box;
  }
  .MuiGrid-zeroMinWidth {
    min-width: 0;
  }
  .MuiGrid-direction-xs-column {
    flex-direction: column;
  }
  .MuiGrid-direction-xs-column-reverse {
    flex-direction: column-reverse;
  }
  .MuiGrid-direction-xs-row-reverse {
    flex-direction: row-reverse;
  }
  .MuiGrid-wrap-xs-nowrap {
    flex-wrap: nowrap;
  }
  .MuiGrid-wrap-xs-wrap-reverse {
    flex-wrap: wrap-reverse;
  }
  .MuiGrid-align-items-xs-center {
    align-items: center;
  }
  .MuiGrid-align-items-xs-flex-start {
    align-items: flex-start;
  }
  .MuiGrid-align-items-xs-flex-end {
    align-items: flex-end;
  }
  .MuiGrid-align-items-xs-baseline {
    align-items: baseline;
  }
  .MuiGrid-align-content-xs-center {
    align-content: center;
  }
  .MuiGrid-align-content-xs-flex-start {
    align-content: flex-start;
  }
  .MuiGrid-align-content-xs-flex-end {
    align-content: flex-end;
  }
  .MuiGrid-align-content-xs-space-between {
    align-content: space-between;
  }
  .MuiGrid-align-content-xs-space-around {
    align-content: space-around;
  }
  .MuiGrid-justify-xs-center {
    justify-content: center;
  }
  .MuiGrid-justify-xs-flex-end {
    justify-content: flex-end;
  }
  .MuiGrid-justify-xs-space-between {
    justify-content: space-between;
  }
  .MuiGrid-justify-xs-space-around {
    justify-content: space-around;
  }
  .MuiGrid-justify-xs-space-evenly {
    justify-content: space-evenly;
  }
  .MuiGrid-spacing-xs-1 {
    width: calc(100% + 8px);
    margin: -4px;
  }
  .MuiGrid-spacing-xs-1 > .MuiGrid-item {
    padding: 4px;
  }
  .MuiGrid-spacing-xs-2 {
    width: calc(100% + 16px);
    margin: -8px;
  }
  .MuiGrid-spacing-xs-2 > .MuiGrid-item {
    padding: 8px;
  }
  .MuiGrid-spacing-xs-3 {
    width: calc(100% + 24px);
    margin: -12px;
  }
  .MuiGrid-spacing-xs-3 > .MuiGrid-item {
    padding: 12px;
  }
  .MuiGrid-spacing-xs-4 {
    width: calc(100% + 32px);
    margin: -16px;
  }
  .MuiGrid-spacing-xs-4 > .MuiGrid-item {
    padding: 16px;
  }
  .MuiGrid-spacing-xs-5 {
    width: calc(100% + 40px);
    margin: -20px;
  }
  .MuiGrid-spacing-xs-5 > .MuiGrid-item {
    padding: 20px;
  }
  .MuiGrid-spacing-xs-6 {
    width: calc(100% + 48px);
    margin: -24px;
  }
  .MuiGrid-spacing-xs-6 > .MuiGrid-item {
    padding: 24px;
  }
  .MuiGrid-spacing-xs-7 {
    width: calc(100% + 56px);
    margin: -28px;
  }
  .MuiGrid-spacing-xs-7 > .MuiGrid-item {
    padding: 28px;
  }
  .MuiGrid-spacing-xs-8 {
    width: calc(100% + 64px);
    margin: -32px;
  }
  .MuiGrid-spacing-xs-8 > .MuiGrid-item {
    padding: 32px;
  }
  .MuiGrid-spacing-xs-9 {
    width: calc(100% + 72px);
    margin: -36px;
  }
  .MuiGrid-spacing-xs-9 > .MuiGrid-item {
    padding: 36px;
  }
  .MuiGrid-spacing-xs-10 {
    width: calc(100% + 80px);
    margin: -40px;
  }
  .MuiGrid-spacing-xs-10 > .MuiGrid-item {
    padding: 40px;
  }
  .MuiGrid-grid-xs-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-xs-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-xs-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-xs-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-xs-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-xs-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-xs-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-xs-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-xs-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-xs-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-xs-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-xs-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-xs-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-xs-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
@media (min-width:600px) {
  .MuiGrid-grid-sm-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-sm-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-sm-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-sm-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-sm-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-sm-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-sm-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-sm-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-sm-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-sm-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-sm-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-sm-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-sm-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-sm-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
@media (min-width:960px) {
  .MuiGrid-grid-md-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-md-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-md-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-md-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-md-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-md-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-md-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-md-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-md-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-md-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-md-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-md-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-md-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-md-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
@media (min-width:1280px) {
  .MuiGrid-grid-lg-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-lg-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-lg-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-lg-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-lg-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-lg-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-lg-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-lg-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-lg-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-lg-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-lg-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-lg-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-lg-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-lg-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
@media (min-width:1920px) {
  .MuiGrid-grid-xl-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-xl-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-xl-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-xl-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-xl-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-xl-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-xl-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-xl-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-xl-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-xl-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-xl-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-xl-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-xl-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-xl-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
@media (min-width:0px) and (max-width:599.95px) {
  .PrivateHiddenCss-onlyXs-29 {
    display: none;
  }
}
@media (min-width:0px) {
  .PrivateHiddenCss-xsUp-30 {
    display: none;
  }
}
@media (max-width:599.95px) {
  .PrivateHiddenCss-xsDown-31 {
    display: none;
  }
}
@media (min-width:600px) and (max-width:959.95px) {
  .PrivateHiddenCss-onlySm-32 {
    display: none;
  }
}
@media (min-width:600px) {
  .PrivateHiddenCss-smUp-33 {
    display: none;
  }
}
@media (max-width:959.95px) {
  .PrivateHiddenCss-smDown-34 {
    display: none;
  }
}
@media (min-width:960px) and (max-width:1279.95px) {
  .PrivateHiddenCss-onlyMd-35 {
    display: none;
  }
}
@media (min-width:960px) {
  .PrivateHiddenCss-mdUp-36 {
    display: none;
  }
}
@media (max-width:1279.95px) {
  .PrivateHiddenCss-mdDown-37 {
    display: none;
  }
}
@media (min-width:1280px) and (max-width:1919.95px) {
  .PrivateHiddenCss-onlyLg-38 {
    display: none;
  }
}
@media (min-width:1280px) {
  .PrivateHiddenCss-lgUp-39 {
    display: none;
  }
}
@media (max-width:1919.95px) {
  .PrivateHiddenCss-lgDown-40 {
    display: none;
  }
}
@media (min-width:1920px) {
  .PrivateHiddenCss-onlyXl-41 {
    display: none;
  }
}
@media (min-width:1920px) {
  .PrivateHiddenCss-xlUp-42 {
    display: none;
  }
}
@media (min-width:0px) {
  .PrivateHiddenCss-xlDown-43 {
    display: none;
  }
}
  .MuiList-root {
    margin: 0;
    padding: 0;
    position: relative;
    list-style: none;
  }
  .MuiList-padding {
    padding-top: 8px;
    padding-bottom: 8px;
  }
  .MuiList-subheader {
    padding-top: 0;
  }
  .MuiListItem-root {
    width: 100%;
    display: flex;
    position: relative;
    box-sizing: border-box;
    text-align: left;
    align-items: center;
    padding-top: 8px;
    padding-bottom: 8px;
    justify-content: flex-start;
    text-decoration: none;
  }
  .MuiListItem-root.Mui-focusVisible {
    background-color: rgba(255, 255, 255, 0.2);
  }
  .MuiListItem-root.Mui-selected, .MuiListItem-root.Mui-selected:hover {
    background-color: rgba(255, 255, 255, 0.2);
  }
  .MuiListItem-root.Mui-disabled {
    opacity: 0.5;
  }
  .MuiListItem-container {
    position: relative;
  }
  .MuiListItem-dense {
    padding-top: 4px;
    padding-bottom: 4px;
  }
  .MuiListItem-alignItemsFlexStart {
    align-items: flex-start;
  }
  .MuiListItem-divider {
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    background-clip: padding-box;
  }
  .MuiListItem-gutters {
    padding-left: 16px;
    padding-right: 16px;
  }
  .MuiListItem-button {
    transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  }
  .MuiListItem-button:hover {
    text-decoration: none;
    background-color: rgba(255, 255, 255, 0.1);
  }
@media (hover: none) {
  .MuiListItem-button:hover {
    background-color: transparent;
  }
}
  .MuiListItem-secondaryAction {
    padding-right: 48px;
  }
  .MuiPopover-paper {
    outline: 0;
    position: absolute;
    max-width: calc(100% - 32px);
    min-width: 16px;
    max-height: calc(100% - 32px);
    min-height: 16px;
    overflow-x: hidden;
    overflow-y: auto;
  }
  .MuiMenu-paper {
    max-height: calc(100% - 96px);
    -webkit-overflow-scrolling: touch;
  }
  .MuiMenu-list {
    outline: 0;
  }
  .MuiSnackbar-root {
    left: 8px;
    right: 8px;
    display: flex;
    z-index: 1400;
    position: fixed;
    align-items: center;
    justify-content: center;
  }
  .MuiSnackbar-anchorOriginTopCenter {
    top: 8px;
  }
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginTopCenter {
    top: 24px;
    left: 50%;
    right: auto;
    transform: translateX(-50%);
  }
}
  .MuiSnackbar-anchorOriginBottomCenter {
    bottom: 8px;
  }
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginBottomCenter {
    left: 50%;
    right: auto;
    bottom: 24px;
    transform: translateX(-50%);
  }
}
  .MuiSnackbar-anchorOriginTopRight {
    top: 8px;
    justify-content: flex-end;
  }
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginTopRight {
    top: 24px;
    left: auto;
    right: 24px;
  }
}
  .MuiSnackbar-anchorOriginBottomRight {
    bottom: 8px;
    justify-content: flex-end;
  }
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginBottomRight {
    left: auto;
    right: 24px;
    bottom: 24px;
  }
}
  .MuiSnackbar-anchorOriginTopLeft {
    top: 8px;
    justify-content: flex-start;
  }
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginTopLeft {
    top: 24px;
    left: 24px;
    right: auto;
  }
}
  .MuiSnackbar-anchorOriginBottomLeft {
    bottom: 8px;
    justify-content: flex-start;
  }
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginBottomLeft {
    left: 24px;
    right: auto;
    bottom: 24px;
  }
}
  .makeStyles-root-1 {
    display: flex;
  }
@media (min-width:600px) {
  .makeStyles-drawer-2 {
    width: 70px;
    flex-shrink: 0;
  }
}
@media (min-width:600px) {
  .makeStyles-appBar-3 {
    width: calc(100% - 70px);
    margin-left: 70px;
  }
}
  .makeStyles-menuButton-4 {
    margin-left: 4px;
  }
@media (min-width:600px) {
  .makeStyles-menuButton-4 {
    display: none;
  }
}
  .makeStyles-toolbar-5 {
    min-height: 56px;
  }
@media (min-width:0px) and (orientation: landscape) {
  .makeStyles-toolbar-5 {
    min-height: 48px;
  }
}
@media (min-width:600px) {
  .makeStyles-toolbar-5 {
    min-height: 64px;
  }
}
  .makeStyles-drawerPaper-6 {
    width: 70px;
  }
  .makeStyles-content-7 {
    padding: 24px;
    flex-grow: 1;
  }</style>
          <script async="" src="./Happy String_files/analytics.js.download"></script><script async="" src="./Happy String_files/analytics.js.download"></script><script async="" src="./Happy String_files/analytics.js.download"></script><script async="" src="./Happy String_files/analytics.js.download"></script><script async="" src="./Happy String_files/analytics.js.download"></script><script async="" src="./Happy String_files/analytics.js.download"></script><script async="" src="./Happy String_files/analytics.js.download"></script><script src="./Happy String_files/bundle.5779895a.js.download" defer=""></script>
      <script charset="utf-8" src="./Happy String_files/0.24074f92.chunk.js.download"></script><script charset="utf-8" src="./Happy String_files/4.d3f00411.chunk.js.download"></script><style data-jss="" data-meta="MuiGrid">
.MuiGrid-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  box-sizing: border-box;
}
.MuiGrid-item {
  margin: 0;
  box-sizing: border-box;
}
.MuiGrid-zeroMinWidth {
  min-width: 0;
}
.MuiGrid-direction-xs-column {
  flex-direction: column;
}
.MuiGrid-direction-xs-column-reverse {
  flex-direction: column-reverse;
}
.MuiGrid-direction-xs-row-reverse {
  flex-direction: row-reverse;
}
.MuiGrid-wrap-xs-nowrap {
  flex-wrap: nowrap;
}
.MuiGrid-wrap-xs-wrap-reverse {
  flex-wrap: wrap-reverse;
}
.MuiGrid-align-items-xs-center {
  align-items: center;
}
.MuiGrid-align-items-xs-flex-start {
  align-items: flex-start;
}
.MuiGrid-align-items-xs-flex-end {
  align-items: flex-end;
}
.MuiGrid-align-items-xs-baseline {
  align-items: baseline;
}
.MuiGrid-align-content-xs-center {
  align-content: center;
}
.MuiGrid-align-content-xs-flex-start {
  align-content: flex-start;
}
.MuiGrid-align-content-xs-flex-end {
  align-content: flex-end;
}
.MuiGrid-align-content-xs-space-between {
  align-content: space-between;
}
.MuiGrid-align-content-xs-space-around {
  align-content: space-around;
}
.MuiGrid-justify-xs-center {
  justify-content: center;
}
.MuiGrid-justify-xs-flex-end {
  justify-content: flex-end;
}
.MuiGrid-justify-xs-space-between {
  justify-content: space-between;
}
.MuiGrid-justify-xs-space-around {
  justify-content: space-around;
}
.MuiGrid-justify-xs-space-evenly {
  justify-content: space-evenly;
}
.MuiGrid-spacing-xs-1 {
  width: calc(100% + 8px);
  margin: -4px;
}
.MuiGrid-spacing-xs-1 > .MuiGrid-item {
  padding: 4px;
}
.MuiGrid-spacing-xs-2 {
  width: calc(100% + 16px);
  margin: -8px;
}
.MuiGrid-spacing-xs-2 > .MuiGrid-item {
  padding: 8px;
}
.MuiGrid-spacing-xs-3 {
  width: calc(100% + 24px);
  margin: -12px;
}
.MuiGrid-spacing-xs-3 > .MuiGrid-item {
  padding: 12px;
}
.MuiGrid-spacing-xs-4 {
  width: calc(100% + 32px);
  margin: -16px;
}
.MuiGrid-spacing-xs-4 > .MuiGrid-item {
  padding: 16px;
}
.MuiGrid-spacing-xs-5 {
  width: calc(100% + 40px);
  margin: -20px;
}
.MuiGrid-spacing-xs-5 > .MuiGrid-item {
  padding: 20px;
}
.MuiGrid-spacing-xs-6 {
  width: calc(100% + 48px);
  margin: -24px;
}
.MuiGrid-spacing-xs-6 > .MuiGrid-item {
  padding: 24px;
}
.MuiGrid-spacing-xs-7 {
  width: calc(100% + 56px);
  margin: -28px;
}
.MuiGrid-spacing-xs-7 > .MuiGrid-item {
  padding: 28px;
}
.MuiGrid-spacing-xs-8 {
  width: calc(100% + 64px);
  margin: -32px;
}
.MuiGrid-spacing-xs-8 > .MuiGrid-item {
  padding: 32px;
}
.MuiGrid-spacing-xs-9 {
  width: calc(100% + 72px);
  margin: -36px;
}
.MuiGrid-spacing-xs-9 > .MuiGrid-item {
  padding: 36px;
}
.MuiGrid-spacing-xs-10 {
  width: calc(100% + 80px);
  margin: -40px;
}
.MuiGrid-spacing-xs-10 > .MuiGrid-item {
  padding: 40px;
}
.MuiGrid-grid-xs-auto {
  flex-grow: 0;
  max-width: none;
  flex-basis: auto;
}
.MuiGrid-grid-xs-true {
  flex-grow: 1;
  max-width: 100%;
  flex-basis: 0;
}
.MuiGrid-grid-xs-1 {
  flex-grow: 0;
  max-width: 8.333333%;
  flex-basis: 8.333333%;
}
.MuiGrid-grid-xs-2 {
  flex-grow: 0;
  max-width: 16.666667%;
  flex-basis: 16.666667%;
}
.MuiGrid-grid-xs-3 {
  flex-grow: 0;
  max-width: 25%;
  flex-basis: 25%;
}
.MuiGrid-grid-xs-4 {
  flex-grow: 0;
  max-width: 33.333333%;
  flex-basis: 33.333333%;
}
.MuiGrid-grid-xs-5 {
  flex-grow: 0;
  max-width: 41.666667%;
  flex-basis: 41.666667%;
}
.MuiGrid-grid-xs-6 {
  flex-grow: 0;
  max-width: 50%;
  flex-basis: 50%;
}
.MuiGrid-grid-xs-7 {
  flex-grow: 0;
  max-width: 58.333333%;
  flex-basis: 58.333333%;
}
.MuiGrid-grid-xs-8 {
  flex-grow: 0;
  max-width: 66.666667%;
  flex-basis: 66.666667%;
}
.MuiGrid-grid-xs-9 {
  flex-grow: 0;
  max-width: 75%;
  flex-basis: 75%;
}
.MuiGrid-grid-xs-10 {
  flex-grow: 0;
  max-width: 83.333333%;
  flex-basis: 83.333333%;
}
.MuiGrid-grid-xs-11 {
  flex-grow: 0;
  max-width: 91.666667%;
  flex-basis: 91.666667%;
}
.MuiGrid-grid-xs-12 {
  flex-grow: 0;
  max-width: 100%;
  flex-basis: 100%;
}
@media (min-width:600px) {
  .MuiGrid-grid-sm-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-sm-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-sm-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-sm-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-sm-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-sm-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-sm-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-sm-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-sm-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-sm-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-sm-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-sm-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-sm-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-sm-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
@media (min-width:960px) {
  .MuiGrid-grid-md-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-md-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-md-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-md-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-md-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-md-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-md-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-md-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-md-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-md-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-md-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-md-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-md-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-md-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
@media (min-width:1280px) {
  .MuiGrid-grid-lg-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-lg-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-lg-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-lg-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-lg-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-lg-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-lg-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-lg-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-lg-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-lg-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-lg-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-lg-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-lg-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-lg-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
@media (min-width:1920px) {
  .MuiGrid-grid-xl-auto {
    flex-grow: 0;
    max-width: none;
    flex-basis: auto;
  }
  .MuiGrid-grid-xl-true {
    flex-grow: 1;
    max-width: 100%;
    flex-basis: 0;
  }
  .MuiGrid-grid-xl-1 {
    flex-grow: 0;
    max-width: 8.333333%;
    flex-basis: 8.333333%;
  }
  .MuiGrid-grid-xl-2 {
    flex-grow: 0;
    max-width: 16.666667%;
    flex-basis: 16.666667%;
  }
  .MuiGrid-grid-xl-3 {
    flex-grow: 0;
    max-width: 25%;
    flex-basis: 25%;
  }
  .MuiGrid-grid-xl-4 {
    flex-grow: 0;
    max-width: 33.333333%;
    flex-basis: 33.333333%;
  }
  .MuiGrid-grid-xl-5 {
    flex-grow: 0;
    max-width: 41.666667%;
    flex-basis: 41.666667%;
  }
  .MuiGrid-grid-xl-6 {
    flex-grow: 0;
    max-width: 50%;
    flex-basis: 50%;
  }
  .MuiGrid-grid-xl-7 {
    flex-grow: 0;
    max-width: 58.333333%;
    flex-basis: 58.333333%;
  }
  .MuiGrid-grid-xl-8 {
    flex-grow: 0;
    max-width: 66.666667%;
    flex-basis: 66.666667%;
  }
  .MuiGrid-grid-xl-9 {
    flex-grow: 0;
    max-width: 75%;
    flex-basis: 75%;
  }
  .MuiGrid-grid-xl-10 {
    flex-grow: 0;
    max-width: 83.333333%;
    flex-basis: 83.333333%;
  }
  .MuiGrid-grid-xl-11 {
    flex-grow: 0;
    max-width: 91.666667%;
    flex-basis: 91.666667%;
  }
  .MuiGrid-grid-xl-12 {
    flex-grow: 0;
    max-width: 100%;
    flex-basis: 100%;
  }
}
</style><style data-jss="" data-meta="MuiTouchRipple">
.MuiTouchRipple-root {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  overflow: hidden;
  position: absolute;
  border-radius: inherit;
  pointer-events: none;
}
.MuiTouchRipple-ripple {
  opacity: 0;
  position: absolute;
}
.MuiTouchRipple-rippleVisible {
  opacity: 0.3;
  animation: MuiTouchRipple-keyframes-enter 550ms cubic-bezier(0.4, 0, 0.2, 1);
  transform: scale(1);
}
.MuiTouchRipple-ripplePulsate {
  animation-duration: 200ms;
}
.MuiTouchRipple-child {
  width: 100%;
  height: 100%;
  display: block;
  opacity: 1;
  border-radius: 50%;
  background-color: currentColor;
}
.MuiTouchRipple-childLeaving {
  opacity: 0;
  animation: MuiTouchRipple-keyframes-exit 550ms cubic-bezier(0.4, 0, 0.2, 1);
}
.MuiTouchRipple-childPulsate {
  top: 0;
  left: 0;
  position: absolute;
  animation: MuiTouchRipple-keyframes-pulsate 2500ms cubic-bezier(0.4, 0, 0.2, 1) 200ms infinite;
}
@-webkit-keyframes MuiTouchRipple-keyframes-enter {
  0% {
    opacity: 0.1;
    transform: scale(0);
  }
  100% {
    opacity: 0.3;
    transform: scale(1);
  }
}
@-webkit-keyframes MuiTouchRipple-keyframes-exit {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@-webkit-keyframes MuiTouchRipple-keyframes-pulsate {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(0.92);
  }
  100% {
    transform: scale(1);
  }
}
</style><style data-jss="" data-meta="MuiButtonBase">
.MuiButtonBase-root {
  color: inherit;
  border: 0;
  cursor: pointer;
  margin: 0;
  display: inline-flex;
  outline: 0;
  padding: 0;
  position: relative;
  align-items: center;
  user-select: none;
  border-radius: 0;
  vertical-align: middle;
  -moz-appearance: none;
  justify-content: center;
  text-decoration: none;
  background-color: transparent;
  -webkit-appearance: none;
  -webkit-tap-highlight-color: transparent;
}
.MuiButtonBase-root::-moz-focus-inner {
  border-style: none;
}
.MuiButtonBase-root.Mui-disabled {
  cursor: default;
  pointer-events: none;
}
</style><style data-jss="" data-meta="MuiButton">
.MuiButton-root {
  color: #fff;
  padding: 6px 16px;
  font-size: 0.875rem;
  min-width: 64px;
  box-sizing: border-box;
  transition: background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,border 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  line-height: 1.75;
  border-radius: 4px;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
}
.MuiButton-root:hover {
  text-decoration: none;
  background-color: rgba(255, 255, 255, 0.1);
}
.MuiButton-root.Mui-disabled {
  color: rgba(255, 255, 255, 0.3);
}
@media (hover: none) {
  .MuiButton-root:hover {
    background-color: transparent;
  }
}
.MuiButton-root:hover.Mui-disabled {
  background-color: transparent;
}
.MuiButton-label {
  width: 100%;
  display: inherit;
  align-items: inherit;
  justify-content: inherit;
}
.MuiButton-text {
  padding: 6px 8px;
}
.MuiButton-textPrimary {
  color: #3f51b5;
}
.MuiButton-textPrimary:hover {
  background-color: rgba(63, 81, 181, 0.1);
}
@media (hover: none) {
  .MuiButton-textPrimary:hover {
    background-color: transparent;
  }
}
.MuiButton-textSecondary {
  color: #00BFA5;
}
.MuiButton-textSecondary:hover {
  background-color: rgba(0, 191, 165, 0.1);
}
@media (hover: none) {
  .MuiButton-textSecondary:hover {
    background-color: transparent;
  }
}
.MuiButton-outlined {
  border: 1px solid rgba(255, 255, 255, 0.23);
  padding: 5px 15px;
}
.MuiButton-outlined.Mui-disabled {
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.MuiButton-outlinedPrimary {
  color: #3f51b5;
  border: 1px solid rgba(63, 81, 181, 0.5);
}
.MuiButton-outlinedPrimary:hover {
  border: 1px solid #3f51b5;
  background-color: rgba(63, 81, 181, 0.1);
}
@media (hover: none) {
  .MuiButton-outlinedPrimary:hover {
    background-color: transparent;
  }
}
.MuiButton-outlinedSecondary {
  color: #00BFA5;
  border: 1px solid rgba(0, 191, 165, 0.5);
}
.MuiButton-outlinedSecondary:hover {
  border: 1px solid #00BFA5;
  background-color: rgba(0, 191, 165, 0.1);
}
.MuiButton-outlinedSecondary.Mui-disabled {
  border: 1px solid rgba(255, 255, 255, 0.3);
}
@media (hover: none) {
  .MuiButton-outlinedSecondary:hover {
    background-color: transparent;
  }
}
.MuiButton-contained {
  color: rgba(0, 0, 0, 0.87);
  box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);
  background-color: #e0e0e0;
}
.MuiButton-contained:hover {
  box-shadow: 0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);
  background-color: #d5d5d5;
}
.MuiButton-contained.Mui-focusVisible {
  box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);
}
.MuiButton-contained:active {
  box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);
}
.MuiButton-contained.Mui-disabled {
  color: rgba(255, 255, 255, 0.3);
  box-shadow: none;
  background-color: rgba(255, 255, 255, 0.12);
}
@media (hover: none) {
  .MuiButton-contained:hover {
    box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);
    background-color: #e0e0e0;
  }
}
.MuiButton-contained:hover.Mui-disabled {
  background-color: rgba(255, 255, 255, 0.12);
}
.MuiButton-containedPrimary {
  color: #fff;
  background-color: #3f51b5;
}
.MuiButton-containedPrimary:hover {
  background-color: #303f9f;
}
@media (hover: none) {
  .MuiButton-containedPrimary:hover {
    background-color: #3f51b5;
  }
}
.MuiButton-containedSecondary {
  color: #ffcc00;
  background-color: #00BFA5;
}
.MuiButton-containedSecondary:hover {
  background-color: rgb(0, 133, 115);
}
@media (hover: none) {
  .MuiButton-containedSecondary:hover {
    background-color: #00BFA5;
  }
}
.MuiButton-disableElevation {
  box-shadow: none;
}
.MuiButton-disableElevation:hover {
  box-shadow: none;
}
.MuiButton-disableElevation.Mui-focusVisible {
  box-shadow: none;
}
.MuiButton-disableElevation:active {
  box-shadow: none;
}
.MuiButton-disableElevation.Mui-disabled {
  box-shadow: none;
}
.MuiButton-colorInherit {
  color: inherit;
  border-color: currentColor;
}
.MuiButton-textSizeSmall {
  padding: 4px 5px;
  font-size: 0.8125rem;
}
.MuiButton-textSizeLarge {
  padding: 8px 11px;
  font-size: 0.9375rem;
}
.MuiButton-outlinedSizeSmall {
  padding: 3px 9px;
  font-size: 0.8125rem;
}
.MuiButton-outlinedSizeLarge {
  padding: 7px 21px;
  font-size: 0.9375rem;
}
.MuiButton-containedSizeSmall {
  padding: 4px 10px;
  font-size: 0.8125rem;
}
.MuiButton-containedSizeLarge {
  padding: 8px 22px;
  font-size: 0.9375rem;
}
.MuiButton-fullWidth {
  width: 100%;
}
.MuiButton-startIcon {
  display: inherit;
  margin-left: -4px;
  margin-right: 8px;
}
.MuiButton-startIcon.MuiButton-iconSizeSmall {
  margin-left: -2px;
}
.MuiButton-endIcon {
  display: inherit;
  margin-left: 8px;
  margin-right: -4px;
}
.MuiButton-endIcon.MuiButton-iconSizeSmall {
  margin-right: -2px;
}
.MuiButton-iconSizeSmall > *:first-child {
  font-size: 18px;
}
.MuiButton-iconSizeMedium > *:first-child {
  font-size: 20px;
}
.MuiButton-iconSizeLarge > *:first-child {
  font-size: 22px;
}
</style><style data-jss="" data-meta="MuiBackdrop">
.MuiBackdrop-root {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  z-index: -1;
  position: fixed;
  align-items: center;
  touch-action: none;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5);
  -webkit-tap-highlight-color: transparent;
}
.MuiBackdrop-invisible {
  background-color: transparent;
}
</style><style data-jss="" data-meta="MuiPaper">
.MuiPaper-root {
  color: #fff;
  transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  background-color: #424242;
}
.MuiPaper-rounded {
  border-radius: 4px;
}
.MuiPaper-outlined {
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.MuiPaper-elevation0 {
  box-shadow: none;
}
.MuiPaper-elevation1 {
  box-shadow: 0px 2px 1px -1px rgba(0,0,0,0.2),0px 1px 1px 0px rgba(0,0,0,0.14),0px 1px 3px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation2 {
  box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation3 {
  box-shadow: 0px 3px 3px -2px rgba(0,0,0,0.2),0px 3px 4px 0px rgba(0,0,0,0.14),0px 1px 8px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation4 {
  box-shadow: 0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation5 {
  box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 5px 8px 0px rgba(0,0,0,0.14),0px 1px 14px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation6 {
  box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation7 {
  box-shadow: 0px 4px 5px -2px rgba(0,0,0,0.2),0px 7px 10px 1px rgba(0,0,0,0.14),0px 2px 16px 1px rgba(0,0,0,0.12);
}
.MuiPaper-elevation8 {
  box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);
}
.MuiPaper-elevation9 {
  box-shadow: 0px 5px 6px -3px rgba(0,0,0,0.2),0px 9px 12px 1px rgba(0,0,0,0.14),0px 3px 16px 2px rgba(0,0,0,0.12);
}
.MuiPaper-elevation10 {
  box-shadow: 0px 6px 6px -3px rgba(0,0,0,0.2),0px 10px 14px 1px rgba(0,0,0,0.14),0px 4px 18px 3px rgba(0,0,0,0.12);
}
.MuiPaper-elevation11 {
  box-shadow: 0px 6px 7px -4px rgba(0,0,0,0.2),0px 11px 15px 1px rgba(0,0,0,0.14),0px 4px 20px 3px rgba(0,0,0,0.12);
}
.MuiPaper-elevation12 {
  box-shadow: 0px 7px 8px -4px rgba(0,0,0,0.2),0px 12px 17px 2px rgba(0,0,0,0.14),0px 5px 22px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation13 {
  box-shadow: 0px 7px 8px -4px rgba(0,0,0,0.2),0px 13px 19px 2px rgba(0,0,0,0.14),0px 5px 24px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation14 {
  box-shadow: 0px 7px 9px -4px rgba(0,0,0,0.2),0px 14px 21px 2px rgba(0,0,0,0.14),0px 5px 26px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation15 {
  box-shadow: 0px 8px 9px -5px rgba(0,0,0,0.2),0px 15px 22px 2px rgba(0,0,0,0.14),0px 6px 28px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation16 {
  box-shadow: 0px 8px 10px -5px rgba(0,0,0,0.2),0px 16px 24px 2px rgba(0,0,0,0.14),0px 6px 30px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation17 {
  box-shadow: 0px 8px 11px -5px rgba(0,0,0,0.2),0px 17px 26px 2px rgba(0,0,0,0.14),0px 6px 32px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation18 {
  box-shadow: 0px 9px 11px -5px rgba(0,0,0,0.2),0px 18px 28px 2px rgba(0,0,0,0.14),0px 7px 34px 6px rgba(0,0,0,0.12);
}
.MuiPaper-elevation19 {
  box-shadow: 0px 9px 12px -6px rgba(0,0,0,0.2),0px 19px 29px 2px rgba(0,0,0,0.14),0px 7px 36px 6px rgba(0,0,0,0.12);
}
.MuiPaper-elevation20 {
  box-shadow: 0px 10px 13px -6px rgba(0,0,0,0.2),0px 20px 31px 3px rgba(0,0,0,0.14),0px 8px 38px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation21 {
  box-shadow: 0px 10px 13px -6px rgba(0,0,0,0.2),0px 21px 33px 3px rgba(0,0,0,0.14),0px 8px 40px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation22 {
  box-shadow: 0px 10px 14px -6px rgba(0,0,0,0.2),0px 22px 35px 3px rgba(0,0,0,0.14),0px 8px 42px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation23 {
  box-shadow: 0px 11px 14px -7px rgba(0,0,0,0.2),0px 23px 36px 3px rgba(0,0,0,0.14),0px 9px 44px 8px rgba(0,0,0,0.12);
}
.MuiPaper-elevation24 {
  box-shadow: 0px 11px 15px -7px rgba(0,0,0,0.2),0px 24px 38px 3px rgba(0,0,0,0.14),0px 9px 46px 8px rgba(0,0,0,0.12);
}
</style><style data-jss="" data-meta="MuiDialog">
@media print {
  .MuiDialog-root {
    position: absolute !important;
  }
}
.MuiDialog-scrollPaper {
  display: flex;
  align-items: center;
  justify-content: center;
}
.MuiDialog-scrollBody {
  overflow-x: hidden;
  overflow-y: auto;
  text-align: center;
}
.MuiDialog-scrollBody:after {
  width: 0;
  height: 100%;
  content: "";
  display: inline-block;
  vertical-align: middle;
}
.MuiDialog-container {
  height: 100%;
  outline: 0;
}
@media print {
  .MuiDialog-container {
    height: auto;
  }
}
.MuiDialog-paper {
  margin: 32px;
  position: relative;
  overflow-y: auto;
}
@media print {
  .MuiDialog-paper {
    box-shadow: none;
    overflow-y: visible;
  }
}
.MuiDialog-paperScrollPaper {
  display: flex;
  max-height: calc(100% - 64px);
  flex-direction: column;
}
.MuiDialog-paperScrollBody {
  display: inline-block;
  text-align: left;
  vertical-align: middle;
}
.MuiDialog-paperWidthFalse {
  max-width: calc(100% - 64px);
}
.MuiDialog-paperWidthXs {
  max-width: 444px;
}
@media (max-width:507.95px) {
  .MuiDialog-paperWidthXs.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthSm {
  max-width: 600px;
}
@media (max-width:663.95px) {
  .MuiDialog-paperWidthSm.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthMd {
  max-width: 960px;
}
@media (max-width:1023.95px) {
  .MuiDialog-paperWidthMd.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthLg {
  max-width: 1280px;
}
@media (max-width:1343.95px) {
  .MuiDialog-paperWidthLg.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthXl {
  max-width: 1920px;
}
@media (max-width:1983.95px) {
  .MuiDialog-paperWidthXl.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperFullWidth {
  width: calc(100% - 64px);
}
.MuiDialog-paperFullScreen {
  width: 100%;
  height: 100%;
  margin: 0;
  max-width: 100%;
  max-height: none;
  border-radius: 0;
}
.MuiDialog-paperFullScreen.MuiDialog-paperScrollBody {
  margin: 0;
  max-width: 100%;
}
</style><style data-jss="" data-meta="MuiPopover">
.MuiPopover-paper {
  outline: 0;
  position: absolute;
  max-width: calc(100% - 32px);
  min-width: 16px;
  max-height: calc(100% - 32px);
  min-height: 16px;
  overflow-x: hidden;
  overflow-y: auto;
}
</style><style data-jss="" data-meta="MuiList">
.MuiList-root {
  margin: 0;
  padding: 0;
  position: relative;
  list-style: none;
}
.MuiList-padding {
  padding-top: 8px;
  padding-bottom: 8px;
}
.MuiList-subheader {
  padding-top: 0;
}
</style><style data-jss="" data-meta="MuiMenu">
.MuiMenu-paper {
  max-height: calc(100% - 96px);
  -webkit-overflow-scrolling: touch;
}
.MuiMenu-list {
  outline: 0;
}
</style><style data-jss="" data-meta="MuiSvgIcon">
.MuiSvgIcon-root {
  fill: currentColor;
  width: 1em;
  height: 1em;
  display: inline-block;
  font-size: 1.5rem;
  transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  flex-shrink: 0;
  user-select: none;
}
.MuiSvgIcon-colorPrimary {
  color: #3f51b5;
}
.MuiSvgIcon-colorSecondary {
  color: #00BFA5;
}
.MuiSvgIcon-colorAction {
  color: #fff;
}
.MuiSvgIcon-colorError {
  color: #f44336;
}
.MuiSvgIcon-colorDisabled {
  color: rgba(255, 255, 255, 0.3);
}
.MuiSvgIcon-fontSizeInherit {
  font-size: inherit;
}
.MuiSvgIcon-fontSizeSmall {
  font-size: 1.25rem;
}
.MuiSvgIcon-fontSizeLarge {
  font-size: 2.1875rem;
}
</style><style data-jss="" data-meta="MuiListItem">
.MuiListItem-root {
  width: 100%;
  display: flex;
  position: relative;
  box-sizing: border-box;
  text-align: left;
  align-items: center;
  padding-top: 8px;
  padding-bottom: 8px;
  justify-content: flex-start;
  text-decoration: none;
}
.MuiListItem-root.Mui-focusVisible {
  background-color: rgba(255, 255, 255, 0.2);
}
.MuiListItem-root.Mui-selected, .MuiListItem-root.Mui-selected:hover {
  background-color: rgba(255, 255, 255, 0.2);
}
.MuiListItem-root.Mui-disabled {
  opacity: 0.5;
}
.MuiListItem-container {
  position: relative;
}
.MuiListItem-dense {
  padding-top: 4px;
  padding-bottom: 4px;
}
.MuiListItem-alignItemsFlexStart {
  align-items: flex-start;
}
.MuiListItem-divider {
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  background-clip: padding-box;
}
.MuiListItem-gutters {
  padding-left: 16px;
  padding-right: 16px;
}
.MuiListItem-button {
  transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiListItem-button:hover {
  text-decoration: none;
  background-color: rgba(255, 255, 255, 0.1);
}
@media (hover: none) {
  .MuiListItem-button:hover {
    background-color: transparent;
  }
}
.MuiListItem-secondaryAction {
  padding-right: 48px;
}
</style><style data-jss="" data-meta="MuiIconButton">
.MuiIconButton-root {
  flex: 0 0 auto;
  color: #fff;
  padding: 12px;
  overflow: visible;
  font-size: 1.5rem;
  text-align: center;
  transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border-radius: 50%;
}
.MuiIconButton-root:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
.MuiIconButton-root.Mui-disabled {
  color: rgba(255, 255, 255, 0.3);
  background-color: transparent;
}
@media (hover: none) {
  .MuiIconButton-root:hover {
    background-color: transparent;
  }
}
.MuiIconButton-edgeStart {
  margin-left: -12px;
}
.MuiIconButton-sizeSmall.MuiIconButton-edgeStart {
  margin-left: -3px;
}
.MuiIconButton-edgeEnd {
  margin-right: -12px;
}
.MuiIconButton-sizeSmall.MuiIconButton-edgeEnd {
  margin-right: -3px;
}
.MuiIconButton-colorInherit {
  color: inherit;
}
.MuiIconButton-colorPrimary {
  color: #3f51b5;
}
.MuiIconButton-colorPrimary:hover {
  background-color: rgba(63, 81, 181, 0.1);
}
@media (hover: none) {
  .MuiIconButton-colorPrimary:hover {
    background-color: transparent;
  }
}
.MuiIconButton-colorSecondary {
  color: #00BFA5;
}
.MuiIconButton-colorSecondary:hover {
  background-color: rgba(0, 191, 165, 0.1);
}
@media (hover: none) {
  .MuiIconButton-colorSecondary:hover {
    background-color: transparent;
  }
}
.MuiIconButton-sizeSmall {
  padding: 3px;
  font-size: 1.125rem;
}
.MuiIconButton-label {
  width: 100%;
  display: flex;
  align-items: inherit;
  justify-content: inherit;
}
</style><style data-jss="" data-meta="MuiCssBaseline">
html {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
*, *::before, *::after {
  box-sizing: inherit;
}
strong, b {
  font-weight: bolder;
}
body {
  color: #fff;
  margin: 0;
  font-size: 0.875rem;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  line-height: 1.43;
  letter-spacing: 0.01071em;
  background-color: rgb(17, 17, 17);
}
@media print {
  body {
    background-color: #fff;
  }
}
body::backdrop {
  background-color: rgb(17, 17, 17);
}
</style><style data-jss="" data-meta="MuiDrawer">
.MuiDrawer-docked {
  flex: 0 0 auto;
}
.MuiDrawer-paper {
  top: 0;
  flex: 1 0 auto;
  height: 100%;
  display: flex;
  outline: 0;
  z-index: 1200;
  position: fixed;
  overflow-y: auto;
  flex-direction: column;
  -webkit-overflow-scrolling: touch;
}
.MuiDrawer-paperAnchorLeft {
  left: 0;
  right: auto;
}
.MuiDrawer-paperAnchorRight {
  left: auto;
  right: 0;
}
.MuiDrawer-paperAnchorTop {
  top: 0;
  left: 0;
  right: 0;
  bottom: auto;
  height: auto;
  max-height: 100%;
}
.MuiDrawer-paperAnchorBottom {
  top: auto;
  left: 0;
  right: 0;
  bottom: 0;
  height: auto;
  max-height: 100%;
}
.MuiDrawer-paperAnchorDockedLeft {
  border-right: 1px solid rgba(255, 255, 255, 0.12);
}
.MuiDrawer-paperAnchorDockedTop {
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}
.MuiDrawer-paperAnchorDockedRight {
  border-left: 1px solid rgba(255, 255, 255, 0.12);
}
.MuiDrawer-paperAnchorDockedBottom {
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
</style><style data-jss="" data-meta="PrivateHiddenCss">
@media (min-width:0px) and (max-width:599.95px) {
  .jss29 {
    display: none;
  }
}
@media (min-width:0px) {
  .jss30 {
    display: none;
  }
}
@media (max-width:599.95px) {
  .jss31 {
    display: none;
  }
}
@media (min-width:600px) and (max-width:959.95px) {
  .jss32 {
    display: none;
  }
}
@media (min-width:600px) {
  .jss33 {
    display: none;
  }
}
@media (max-width:959.95px) {
  .jss34 {
    display: none;
  }
}
@media (min-width:960px) and (max-width:1279.95px) {
  .jss35 {
    display: none;
  }
}
@media (min-width:960px) {
  .jss36 {
    display: none;
  }
}
@media (max-width:1279.95px) {
  .jss37 {
    display: none;
  }
}
@media (min-width:1280px) and (max-width:1919.95px) {
  .jss38 {
    display: none;
  }
}
@media (min-width:1280px) {
  .jss39 {
    display: none;
  }
}
@media (max-width:1919.95px) {
  .jss40 {
    display: none;
  }
}
@media (min-width:1920px) {
  .jss41 {
    display: none;
  }
}
@media (min-width:1920px) {
  .jss42 {
    display: none;
  }
}
@media (min-width:0px) {
  .jss43 {
    display: none;
  }
}
</style><style data-jss="" data-meta="makeStyles">
.jss1 {
  display: flex;
}
@media (min-width:600px) {
  .jss2 {
    width: 70px;
    flex-shrink: 0;
  }
}
@media (min-width:600px) {
  .jss3 {
    width: calc(100% - 70px);
    margin-left: 70px;
  }
}
.jss4 {
  margin-left: 4px;
}
@media (min-width:600px) {
  .jss4 {
    display: none;
  }
}
.jss5 {
  min-height: 56px;
}
@media (min-width:0px) and (orientation: landscape) {
  .jss5 {
    min-height: 48px;
  }
}
@media (min-width:600px) {
  .jss5 {
    min-height: 64px;
  }
}
.jss6 {
  width: 70px;
}
.jss7 {
  padding: 24px;
  flex-grow: 1;
}
</style><style data-jss="" data-meta="MuiSnackbar">
.MuiSnackbar-root {
  left: 8px;
  right: 8px;
  display: flex;
  z-index: 1400;
  position: fixed;
  align-items: center;
  justify-content: center;
}
.MuiSnackbar-anchorOriginTopCenter {
  top: 8px;
}
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginTopCenter {
    top: 24px;
    left: 50%;
    right: auto;
    transform: translateX(-50%);
  }
}
.MuiSnackbar-anchorOriginBottomCenter {
  bottom: 8px;
}
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginBottomCenter {
    left: 50%;
    right: auto;
    bottom: 24px;
    transform: translateX(-50%);
  }
}
.MuiSnackbar-anchorOriginTopRight {
  top: 8px;
  justify-content: flex-end;
}
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginTopRight {
    top: 24px;
    left: auto;
    right: 24px;
  }
}
.MuiSnackbar-anchorOriginBottomRight {
  bottom: 8px;
  justify-content: flex-end;
}
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginBottomRight {
    left: auto;
    right: 24px;
    bottom: 24px;
  }
}
.MuiSnackbar-anchorOriginTopLeft {
  top: 8px;
  justify-content: flex-start;
}
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginTopLeft {
    top: 24px;
    left: 24px;
    right: auto;
  }
}
.MuiSnackbar-anchorOriginBottomLeft {
  bottom: 8px;
  justify-content: flex-start;
}
@media (min-width:600px) {
  .MuiSnackbar-anchorOriginBottomLeft {
    left: 24px;
    right: auto;
    bottom: 24px;
  }
}
</style><link rel="stylesheet" type="text/css" href="./Happy String_files/2.3571ec4b.chunk.css"><script charset="utf-8" src="./Happy String_files/2.eb5cc3aa.chunk.js.download"></script><link rel="stylesheet" type="text/css" href="./Happy String_files/3.d09d21a7.chunk.css"><script charset="utf-8" src="./Happy String_files/3.a7f0cc35.chunk.js.download"></script><script id="_carbonads_projs" type="text/javascript" src="./Happy String_files/CK7D55QI.json"></script></head>
      <body style="">
          <div id="root"><div class="root" data-theme="light"><div class="makeStyles-root-1"><div style="position:fixed;z-index:10"> <button class="MuiButtonBase-root MuiIconButton-root makeStyles-menuButton-4 MuiIconButton-colorInherit MuiIconButton-edgeStart" tabindex="0" type="button" aria-label="open drawer"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="presentation"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg></span></button></div><nav class="makeStyles-drawer-2" aria-label="mailbox folders"><div class="PrivateHiddenCss-smUp-33"></div><div class="PrivateHiddenCss-xsDown-31"><div class="MuiDrawer-root MuiDrawer-docked"><div class="MuiPaper-root MuiDrawer-paper makeStyles-drawerPaper-6 MuiDrawer-paperAnchorLeft MuiDrawer-paperAnchorDockedLeft MuiPaper-elevation0"><div id="sideBar" class="sidebar"><div class="makeStyles-toolbar-5"><div style="height:45px;box-sizing:border-box;padding:10px;text-align:center"><a style="display:inline-block" href="https://code.dcoder.tech/"><div class="logoIcon"><img src="./Happy String_files/logo_dcoder.93662c17.png" style="height:100%;width:100%;padding:4.5px;box-sizing:border-box"></div></a></div></div><ul class="MuiList-root MuiList-padding"><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding:0"><a style="color:lightgray;text-decoration:none;width:100%" title="Feed" href="https://code.dcoder.tech/feed"><div class="barIcon"><span class="icon icon-feed"></span><div style="text-align:center;font-size:8px">Feed</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding:0"><a style="color:lightgray;text-decoration:none;width:100%" title="My Files" href="https://code.dcoder.tech/files"><div class="barIcon"><span class="icon icon-file"></span><div style="text-align:center;font-size:8px">My Files</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding:0"><a style="color:lightgray;text-decoration:none;width:100%" title="Challenges" href="https://code.dcoder.tech/challenges"><div class="barIcon"><i class="icon icon-challenge"></i><div style="text-align:center;font-size:8px">Challenges</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding:0"><a style="color:lightgray;text-decoration:none;width:100%" title="Leaderboard" href="https://code.dcoder.tech/leaderboard"><div class="barIcon"><span class="icon icon-leaderboard"></span><div style="text-align:center;font-size:8px">Leaderboard</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding:0"><a style="color:lightgray;text-decoration:none;width:100%" title="Dev Chat" href="https://code.dcoder.tech/devchat"><div class="barIcon"><i class="icon icon-devchat"></i><div style="text-align:center;font-size:8px">Dev Chat</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding:0"><a style="color:lightgray;text-decoration:none;width:100%" title="Settings" href="https://code.dcoder.tech/settings/profile"><div class="barIcon"><i class="icon icon-setting"></i><div style="text-align:center;font-size:8px">Settings</div></div></a><span class="MuiTouchRipple-root"></span></div></ul><a style="color:lightgray;text-decoration:none;width:100%" href="https://code.dcoder.tech/profile/shayaan7"><div style="position:absolute;bottom:10px" class="barIcon last"><img src="./Happy String_files/photo.jpg" alt="profile pic" style="height:30px;width:30px;border-radius:50%"><div style="text-align:center;font-size:10px;overflow:hidden;text-overflow:ellipsis;padding:0px 5px">@<!-- -->shayaan7</div></div></a></div></div></div></div></nav><div><div style="height:100%;overflow:hidden"></div></div></div><div class="main-container"><div><div class="MuiGrid-root MuiGrid-container" style="height: 100%;"><div class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-4 MuiGrid-grid-md-3" style="display: block;"><div class="bg-2" style="height: 100vh;"><div style="display: flex; align-items: center; height: 45px; padding: 10px; font-weight: bold; border-bottom: 1px solid black;"><h1 class="nav-heading text-color" style="font-size: 16px;">Happy String</h1></div><div class="side-subnav"><div><div style="height: calc(100vh - 45px); box-sizing: border-box; padding: 15px; overflow: auto;"><div class="questionHeading text-color ">Problem Description:</div><div class="questionDescription"><pre class="questionSubDescription description-text-color">A happy string is a string in which each character is lexicographically greater than its next character. You are given a positive integer N as an input. You need to print the smallest lexicographical string possible of length N.
NOTE: All characters in a happy string are in lowercase.</pre></div><br><div class="questionHeading text-color">Input:</div><div class="questionDescription"><pre class="questionSubDescription description-text-color">A single integer N.</pre></div><br><div class="questionHeading text-color">Output:</div><div class="questionDescription"><pre class="questionSubDescription description-text-color">Print the lexicographically smallest string of length N.</pre></div><br><div class="questionHeading text-color">Constraints:</div><div class="questionDescription"><pre class="questionSubDescription description-text-color">1 ≤ N ≤ 26 </pre></div><br><div class="questionHeading text-color">Sample Input:</div><div class="questionDescription"><pre class="questionIODescription description-text-color">2</pre></div><br><div class="questionHeading text-color">Sample Output:</div><div class="questionDescription"><pre class="questionIODescription description-text-color">ba</pre></div></div></div></div></div></div><div class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-8 MuiGrid-grid-md-9" style="height: 100%;"><div style="height: 100vh; position: relative;"><div class="background-color-2 text-color" style="align-items: center; display: flex; box-sizing: border-box; padding: 10px; height: 45px; font-weight: bold; border-bottom: 1px solid black;"><div>Editor</div><button class="MuiButtonBase-root MuiButton-root MuiButton-contained run-button MuiButton-containedSizeSmall MuiButton-sizeSmall" tabindex="0" type="button" style="margin-left: 50px;"><span class="MuiButton-label"><span class="MuiButton-startIcon MuiButton-iconSizeSmall"><i class="fas fa-play-circle">  </i></span>Run code</span><span class="MuiTouchRipple-root"></span></button><div style="margin-left: auto;"><button class="MuiButtonBase-root MuiButton-root MuiButton-contained button-color MuiButton-containedSizeSmall MuiButton-sizeSmall" tabindex="0" type="button"><span class="MuiButton-label"><span class="MuiButton-startIcon MuiButton-iconSizeSmall"><i class="far fa-dot-circle" style="display: inline-block; vertical-align: middle;">  </i></span>Input<span class="MuiButton-endIcon MuiButton-iconSizeSmall"><i class="fa fa-upload" style="display: inline-block; vertical-align: middle;">  </i></span></span><span class="MuiTouchRipple-root"></span></button><button class="MuiButtonBase-root MuiIconButton-root" tabindex="0" type="button" aria-label="More" aria-haspopup="true" style="padding: 0px 5px;"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="presentation"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></button></div></div><div style="height: calc(100% - 45px);"><div class="terminalTop-border"><div class="MuiGrid-root MuiGrid-container" style="height: 100%;"><div class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-12 MuiGrid-grid-md-12"><div style="position: relative;"><div style="margin: 0px; padding: 0px;"><div class="react-codemirror2"><div class="CodeMirror cm-s-monokai CodeMirror-focused" style="width: 100%; height: 537px; font-size: 14px;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 4px; left: 43px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 39px; margin-bottom: -5px; border-right-width: 25px; min-height: 168px; min-width: 870.672px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre>x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 0px; width: 925px; height: 20px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 140px; width: 86.375px; height: 20px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 20px; width: 925px; height: 120px;"></div></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 20px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">N</span><span class="cm-operator">=</span><span class="cm-builtin">input</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">i</span><span class="cm-operator">=</span><span class="cm-number">0</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">p</span><span class="cm-operator">=</span>[<span class="cm-variable">N</span>]</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">list</span><span class="cm-operator">=</span>[<span class="cm-string">"a"</span>,<span class="cm-string">"b"</span>,<span class="cm-string">"c"</span>,<span class="cm-string">"d"</span>,<span class="cm-string">"e"</span>,<span class="cm-string">"f"</span>,<span class="cm-string">"g"</span>,<span class="cm-string">"h"</span>,<span class="cm-string">"i"</span>,<span class="cm-string">"j"</span>,<span class="cm-string">"k"</span>,<span class="cm-string">"l"</span>,<span class="cm-string">"m"</span>,<span class="cm-string">"n"</span>,<span class="cm-string">"o"</span>,<span class="cm-string">"p"</span>,<span class="cm-string">"q"</span>,<span class="cm-string">"r"</span>,<span class="cm-string">"s"</span>,<span class="cm-string">"t"</span>,<span class="cm-string">"u"</span>,<span class="cm-string">"v"</span>,<span class="cm-string">"w"</span>,<span class="cm-string">"x"</span>,<span class="cm-string">"y"</span>,<span class="cm-string">"z"</span>]</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div><div class="CodeMirror-gutter-elt" style="left: 29px; width: 10px;"><div class="CodeMirror-foldgutter-open CodeMirror-guttermarker-subtle"></div></div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">for</span> <span class="cm-variable">i</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-builtin">int</span>(<span class="cm-variable">N</span>)):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">6</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">p</span>[<span class="cm-variable">i</span>] <span class="cm-operator">=</span> <span class="cm-builtin">list</span>[<span class="cm-variable">i</span>]</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">7</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ans</span><span class="cm-operator">=</span><span class="cm-builtin">reversed</span>(<span class="cm-variable">p</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -39px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">8</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-operator">*</span><span class="cm-variable">ans</span>)</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 25px; width: 1px; border-bottom: 0px solid transparent; top: 168px;"></div><div class="CodeMirror-gutters" style="height: 193px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div><div class="CodeMirror-gutter CodeMirror-foldgutter"></div></div></div></div></div><div style="height: 26px; color: rgb(189, 189, 189); text-align: right; font-family: Quicksand, sans-serif; font-size: 13px; background-color: rgb(39, 40, 34); padding: 5px 10px;"><span style="display: none; float: left;"></span>Line: 1 Col: 0</div></div></div></div></div></div></div></div></div></div><div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></div></div></div></div>
          <script>
          window.__PRELOADED_STATE__ ={"questionList":{"easy":{"message":"question List Page Number 1","page_no":1,"data":[{"_id":"5e1086efa1312802b296d39f","problem_setter":{"id":"5de25e832fcfb665c5f6593e","name":"Saurav Chandra"},"level":"easy","title":"Floating Number","question":"Bob has a floating point number N. He wants to set the precision for 2 digits after the decimal point for the number.\nHe is not good at coding, hence looking for your help.","input":"The first line contains T, the number of test cases.\nNext T line contains floating point number N.","output":"Print N in a separate line after setting precision for 2 digits after the decimal point:\n","constraints":"1 <= T <= 1000\n1 <= N <= 10000","sample_input":"1\n713.166\n","sample_output":"713.17\n","max_marks":4,"approved_at":"2020-06-15T14:13:32.171Z","solved_by":1240},{"_id":"5b757d9d791e284892a42b4a","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"SwapMaster solves Symmetric Swap","question":"The SwapMaster is known to be the greatest and fastest swapper of all time. You intend to bring him down and become the new SwapMaster of the city. Through some secret sources, you found out that The SwapMaster undertook yet another task from Dr. Symmetry. The task he undertook is to perform a Symmetric Swap on an array A of numbers. Perform this task before SwapMaster to become the new SwapMaster.\nA Symmetric Swap involves swapping a number in an array with its symmetric position in the array.\nFor example, if you want to swap element at position 2, you will swap it with the 2nd element from the back of the array.","input":"First line contains N, denoting the number of elements in the array A.\nNext line contains N space-separated positive numbers.","output":"Print the array after performing the Symmetric Swap on it.","constraints":"2 ≤ N ≤ 100\n1 ≤ A[i] ≤ 1000","sample_input":"6\n1 2 3 4 5 6","sample_output":"6 5 4 3 2 1","max_marks":4,"approved_at":"2019-12-28T17:27:05.653Z","solved_by":2527},{"_id":"5b211869ac71d7305eae7965","problem_setter":{"id":"5b18fcf7be95b1e1644787c0","name":"Bhanu Nadar"},"level":"easy","title":"String Matching","question":"Cody has a sequence of characters N. He likes a sequence if it contains his favourite sequence as a substring.\nGiven the sequence and his favourite sequence F, check whether the favourite sequence is present in the sequence.","input":"The first line of input contains a single line T, which represents the number of test cases. \nEach test case consists of 2 strings separated by space N and F respectively.","output":"Print \"Yes\" if the sequence contains the favorite sequence in it, otherwise print \"No\".","constraints":"1<=T<=10.\n1<=|N|,|F|<=100.\nAll the characters are lowercase alphabets.","sample_input":"2\nabcde abc\npqrst pr","sample_output":"Yes\nNo","max_marks":3,"approved_at":"2019-12-16T05:53:27.828Z","solved_by":1238},{"_id":"5b28ea8562db8b46ab2ac711","problem_setter":{"id":"5b18fcf7be95b1e1644787c0","name":"Bhanu Nadar"},"level":"easy","title":"Leap Year","question":"Steve is playing a quiz game with his brother John. As Steve just learned the concept of leap year, John wanted to test his knowledge. For that, John started to ask Steve whether a year is a leap year or not by giving him a random year. Steve is little confused and he asks your help to the quiz.\n","input":"The first line of input contains one integer T.\n Next T lines will have years given by John.","output":"For each test case print \"Yes\" if it is a leap year else \"No\".","constraints":"1<=T<=100.\n10^3<=Year<=10^5.","sample_input":"2\n2000\n2017","sample_output":"Yes\nNo","max_marks":6,"approved_at":"2019-11-29T12:29:32.302Z","solved_by":1986},{"_id":"5cf3f4881681076686eade89","problem_setter":{"id":"5cd66e431681076686ea28c6","name":"Rajat Gupta"},"level":"easy","title":"Project Teams","question":"There are N students in a class and Teacher want to divide these students into some groups . Teacher told  that groups consisting of two or less students not allowed , so Teacher want to have as many groups consisting of three or more students as possible.\n\nDivide the students so that the number of groups consisting of three or more students is maximized.","input":"Single integer N\n","output":"Maximum number of groups can be formed","constraints":"1<=N<100000","sample_input":"6","sample_output":"2","max_marks":5,"approved_at":"2019-10-12T09:19:44.526Z","solved_by":3070},{"_id":"5b85bc2bb6415039901fa9d4","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Circle of Numbers","question":"All numbers in NumberLand are standing in a circle for a dancing ceremony. Every number needs a dancing partner. Dancing partner of any number is the number which is standing radially opposite to it in the circle. The numbers are from 0 to N-1. A certain number X wants to know who will be its dancing partner. Please help X.","input":"Two positive integers denoting the value of N and X.","output":"Print the number radially opposite to X in a circle of N numbers.","constraints":"4 ≤ N ≤ 20\n0 ≤ X < N","sample_input":"8 2","sample_output":"6","max_marks":6,"approved_at":"2019-09-14T08:33:39.093Z","solved_by":2141},{"_id":"5b5ee71361601549b1d0b92b","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Happy String","question":"A happy string is a string in which each character is lexicographically greater than its next character. You are given a positive integer N as an input. You need to print the smallest lexicographical string possible of length N.\nNOTE: All characters in a happy string are in lowercase.","input":"A single integer N.","output":"Print the lexicographically smallest string of length N.","constraints":"1 ≤ N ≤ 26 ","sample_input":"2","sample_output":"ba","max_marks":4,"approved_at":"2019-09-09T06:22:37.368Z","solved_by":1555},{"_id":"5b2ecdfea5c3787cda197fde","problem_setter":{"id":"5b18fcf7be95b1e1644787c0","name":"Bhanu Nadar"},"level":"easy","title":"Degree Celsius","question":"Tom is a scientist. He uses huge machines for complex calculations. There is a problem, the machines takes input as Fahrenheit and Tom has the temperatures in Degree Celsius. As he is busy with his work, he asks your help to convert Degree Celsius to Fahrenheit.","input":"The first and only line of the input consists of a single integer T denoting temperature in Degree Celsius.","output":"Print an integer denoting temperature in Fahrenheit.","constraints":"0<=T<=1000","sample_input":"100","sample_output":"212","max_marks":4,"approved_at":"2019-08-07T07:39:14.168Z","solved_by":3578},{"_id":"5b6e530365139d414b2a683e","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Three's Company","question":"This problem requires you to create a output string from input string such that for every character in input string, there are three same characters in output string.","input":"First line contains N, the number of letters in the string.\nThe next line contains the string.","output":"Print the output_string.","constraints":"1 ≤ N ≤ 20","sample_input":"5\nHello","sample_output":"HHHeeellllllooo","max_marks":4,"approved_at":"2019-07-13T14:08:37.510Z","solved_by":2468},{"_id":"5b61e933527d3b5ac5cecda3","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Array Sum","question":"You are given an integer array and you have to find the sum of the elements of the array and find the remainder when the sum is divided by the largest number of the array.","input":"First line contains N, the number of elements. Next line contains N space separated integers (elements of the array).","output":"Print the remainder when sum is divided by the maximum element.","constraints":"1 ≤ n ≤ 100\n0 ≤ A[i] ≤ 1000","sample_input":"5\n1 2 3 4 5","sample_output":"0","max_marks":4,"approved_at":"2019-07-06T13:16:30.092Z","solved_by":2415}],"count":84,"pages":9,"success":true,"list":[{"_id":"5e1086efa1312802b296d39f","problem_setter":{"id":"5de25e832fcfb665c5f6593e","name":"Saurav Chandra"},"level":"easy","title":"Floating Number","question":"Bob has a floating point number N. He wants to set the precision for 2 digits after the decimal point for the number.\nHe is not good at coding, hence looking for your help.","input":"The first line contains T, the number of test cases.\nNext T line contains floating point number N.","output":"Print N in a separate line after setting precision for 2 digits after the decimal point:\n","constraints":"1 <= T <= 1000\n1 <= N <= 10000","sample_input":"1\n713.166\n","sample_output":"713.17\n","max_marks":4,"approved_at":"2020-06-15T14:13:32.171Z","solved_by":1240},{"_id":"5b757d9d791e284892a42b4a","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"SwapMaster solves Symmetric Swap","question":"The SwapMaster is known to be the greatest and fastest swapper of all time. You intend to bring him down and become the new SwapMaster of the city. Through some secret sources, you found out that The SwapMaster undertook yet another task from Dr. Symmetry. The task he undertook is to perform a Symmetric Swap on an array A of numbers. Perform this task before SwapMaster to become the new SwapMaster.\nA Symmetric Swap involves swapping a number in an array with its symmetric position in the array.\nFor example, if you want to swap element at position 2, you will swap it with the 2nd element from the back of the array.","input":"First line contains N, denoting the number of elements in the array A.\nNext line contains N space-separated positive numbers.","output":"Print the array after performing the Symmetric Swap on it.","constraints":"2 ≤ N ≤ 100\n1 ≤ A[i] ≤ 1000","sample_input":"6\n1 2 3 4 5 6","sample_output":"6 5 4 3 2 1","max_marks":4,"approved_at":"2019-12-28T17:27:05.653Z","solved_by":2527},{"_id":"5b211869ac71d7305eae7965","problem_setter":{"id":"5b18fcf7be95b1e1644787c0","name":"Bhanu Nadar"},"level":"easy","title":"String Matching","question":"Cody has a sequence of characters N. He likes a sequence if it contains his favourite sequence as a substring.\nGiven the sequence and his favourite sequence F, check whether the favourite sequence is present in the sequence.","input":"The first line of input contains a single line T, which represents the number of test cases. \nEach test case consists of 2 strings separated by space N and F respectively.","output":"Print \"Yes\" if the sequence contains the favorite sequence in it, otherwise print \"No\".","constraints":"1<=T<=10.\n1<=|N|,|F|<=100.\nAll the characters are lowercase alphabets.","sample_input":"2\nabcde abc\npqrst pr","sample_output":"Yes\nNo","max_marks":3,"approved_at":"2019-12-16T05:53:27.828Z","solved_by":1238},{"_id":"5b28ea8562db8b46ab2ac711","problem_setter":{"id":"5b18fcf7be95b1e1644787c0","name":"Bhanu Nadar"},"level":"easy","title":"Leap Year","question":"Steve is playing a quiz game with his brother John. As Steve just learned the concept of leap year, John wanted to test his knowledge. For that, John started to ask Steve whether a year is a leap year or not by giving him a random year. Steve is little confused and he asks your help to the quiz.\n","input":"The first line of input contains one integer T.\n Next T lines will have years given by John.","output":"For each test case print \"Yes\" if it is a leap year else \"No\".","constraints":"1<=T<=100.\n10^3<=Year<=10^5.","sample_input":"2\n2000\n2017","sample_output":"Yes\nNo","max_marks":6,"approved_at":"2019-11-29T12:29:32.302Z","solved_by":1986},{"_id":"5cf3f4881681076686eade89","problem_setter":{"id":"5cd66e431681076686ea28c6","name":"Rajat Gupta"},"level":"easy","title":"Project Teams","question":"There are N students in a class and Teacher want to divide these students into some groups . Teacher told  that groups consisting of two or less students not allowed , so Teacher want to have as many groups consisting of three or more students as possible.\n\nDivide the students so that the number of groups consisting of three or more students is maximized.","input":"Single integer N\n","output":"Maximum number of groups can be formed","constraints":"1<=N<100000","sample_input":"6","sample_output":"2","max_marks":5,"approved_at":"2019-10-12T09:19:44.526Z","solved_by":3070},{"_id":"5b85bc2bb6415039901fa9d4","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Circle of Numbers","question":"All numbers in NumberLand are standing in a circle for a dancing ceremony. Every number needs a dancing partner. Dancing partner of any number is the number which is standing radially opposite to it in the circle. The numbers are from 0 to N-1. A certain number X wants to know who will be its dancing partner. Please help X.","input":"Two positive integers denoting the value of N and X.","output":"Print the number radially opposite to X in a circle of N numbers.","constraints":"4 ≤ N ≤ 20\n0 ≤ X < N","sample_input":"8 2","sample_output":"6","max_marks":6,"approved_at":"2019-09-14T08:33:39.093Z","solved_by":2141},{"_id":"5b5ee71361601549b1d0b92b","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Happy String","question":"A happy string is a string in which each character is lexicographically greater than its next character. You are given a positive integer N as an input. You need to print the smallest lexicographical string possible of length N.\nNOTE: All characters in a happy string are in lowercase.","input":"A single integer N.","output":"Print the lexicographically smallest string of length N.","constraints":"1 ≤ N ≤ 26 ","sample_input":"2","sample_output":"ba","max_marks":4,"approved_at":"2019-09-09T06:22:37.368Z","solved_by":1555},{"_id":"5b2ecdfea5c3787cda197fde","problem_setter":{"id":"5b18fcf7be95b1e1644787c0","name":"Bhanu Nadar"},"level":"easy","title":"Degree Celsius","question":"Tom is a scientist. He uses huge machines for complex calculations. There is a problem, the machines takes input as Fahrenheit and Tom has the temperatures in Degree Celsius. As he is busy with his work, he asks your help to convert Degree Celsius to Fahrenheit.","input":"The first and only line of the input consists of a single integer T denoting temperature in Degree Celsius.","output":"Print an integer denoting temperature in Fahrenheit.","constraints":"0<=T<=1000","sample_input":"100","sample_output":"212","max_marks":4,"approved_at":"2019-08-07T07:39:14.168Z","solved_by":3578},{"_id":"5b6e530365139d414b2a683e","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Three's Company","question":"This problem requires you to create a output string from input string such that for every character in input string, there are three same characters in output string.","input":"First line contains N, the number of letters in the string.\nThe next line contains the string.","output":"Print the output_string.","constraints":"1 ≤ N ≤ 20","sample_input":"5\nHello","sample_output":"HHHeeellllllooo","max_marks":4,"approved_at":"2019-07-13T14:08:37.510Z","solved_by":2468},{"_id":"5b61e933527d3b5ac5cecda3","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Array Sum","question":"You are given an integer array and you have to find the sum of the elements of the array and find the remainder when the sum is divided by the largest number of the array.","input":"First line contains N, the number of elements. Next line contains N space separated integers (elements of the array).","output":"Print the remainder when sum is divided by the maximum element.","constraints":"1 ≤ n ≤ 100\n0 ≤ A[i] ≤ 1000","sample_input":"5\n1 2 3 4 5","sample_output":"0","max_marks":4,"approved_at":"2019-07-06T13:16:30.092Z","solved_by":2415}]},"medium":null,"hard":null},"activeQuestion":{"_id":"5b85bc2bb6415039901fa9d4","problem_setter":{"id":"5b18fb71be95b1e1644787bc","name":"Mrudul Sankhere"},"level":"easy","title":"Circle of Numbers","question":"All numbers in NumberLand are standing in a circle for a dancing ceremony. Every number needs a dancing partner. Dancing partner of any number is the number which is standing radially opposite to it in the circle. The numbers are from 0 to N-1. A certain number X wants to know who will be its dancing partner. Please help X.","input":"Two positive integers denoting the value of N and X.","output":"Print the number radially opposite to X in a circle of N numbers.","constraints":"4 ≤ N ≤ 20\n0 ≤ X < N","sample_input":"8 2","sample_output":"6","max_marks":6,"approved_at":"2019-09-14T08:33:39.093Z","solved_by":2141},"activeFile":"","editor":{"editorInstance":null,"editorConfig":{"theme":"dark","fontSize":14,"keymap":"sublime"},"outputStatus":false,"editorSetting":false},"leaderBoard":{"list":[{"user_name":"Marek K","user_username":"mkulfi2","user_image_url":"https://dcoder.tech/avatar/dev2.png","user_score":1662,"rank":1},{"user_name":"Jerry","user_username":"jerry","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GibN66V0WWPPCpq8TJXuFRNAuXJyeU3sdI5qwvFnA=s96-c","user_score":1662,"rank":1},{"user_name":"ANKAN mahapatra","user_username":"ankanmahapatra","user_image_url":"https://lh5.googleusercontent.com/-reBqy032CL0/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucl_A0rfeOQ9QTWi428u9EZ3aZ91ew/s96-c/photo.jpg","user_score":1662,"rank":1},{"user_name":"Shubhendra Kushwaha","user_username":"theshubhendra","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GgkjLnKr6_sDfHsHLpXhiny6VZ5lrdKrLkI1Mjgwg8=s96-c","user_score":1634,"rank":4},{"user_name":"Rodrigo Ikegami","user_username":"aimnos","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Ghc8CCU8nB5_vUNmN7djVOEgAS-8vCArUv-ET5x_o8=s96-c","user_score":1600,"rank":5},{"user_name":"Florent","user_username":"labou77","user_image_url":"http://dcoder.tech/avatar/dev2.png","user_score":1593,"rank":6},{"user_name":"Igor Dragushhak","user_username":"dragushhakigor","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Giy9DjUnP7fxDpN-VsGI7D4w7DTZM3d-rn6PWjx=s96-c","user_score":1573,"rank":7},{"user_name":"Marek Vrana","user_username":"marek.vrana1","user_image_url":"https://lh4.googleusercontent.com/-Y7MBqQmhPa0/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rfaD9NPHT9Ds9J4xgGHrsnLYKMVPA/s96-c/photo.jpg","user_score":1565,"rank":8},{"user_name":"angel","user_username":"angel115","user_image_url":"https://dcoder.tech/avatar/dev3.png","user_score":1560,"rank":9},{"user_name":"Vaibhav","user_username":"vksinha","user_image_url":"https://dcoder.tech/avatar/dev7.png","user_score":1560,"rank":9},{"user_name":"Vibhay Singh","user_username":"vibhay_4","user_image_url":"https://dcoder.tech/avatar/dev2.png","user_score":1547,"rank":11},{"user_name":"Vivek Raj","user_username":"vivekrajsundar","user_image_url":"https://lh3.googleusercontent.com/a-/AAuE7mCk8kSaDR4a0npXsF0dbPToTrhwoY-08tkfCeRDDg=s96-c","user_score":1546,"rank":12},{"user_name":"rdots","user_username":"bhaddaka","user_image_url":"https://dcoder.tech/avatar/dev7.png","user_score":1536,"rank":13},{"user_name":"Petar Popović","user_username":"streberko","user_image_url":"https://dcoder.tech/avatar/dev7.png","user_score":1536,"rank":13},{"user_name":"Mónika Pitz","user_username":"pitzmoni","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Gg13UAiX5vYs1R2LmWRrlZpF-mIMmV81tavlDmH_1M=s96-c","user_score":1536,"rank":13},{"user_name":"broken happy","user_username":"brokenhappy","user_image_url":"https://lh4.googleusercontent.com/-ZeRdtcL_NJM/AAAAAAAAAAI/AAAAAAAALUk/AMZuucn8HtnGwRAO2hIV0ZsXZcATbMR9yA/s96-c/photo.jpg","user_score":1525,"rank":16},{"user_name":"Peter M","user_username":"belfast","user_image_url":"https://dcoder.tech/avatar/dev2.png","user_score":1524,"rank":17},{"user_name":"Kawari","user_username":"curtil.guillaume","user_score":1513,"rank":18},{"user_name":"Владимир Кривенков","user_username":"krovyaka","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GgRdVCzszT23OEqfpr4dvQxqtlwZpOKNt9I5aOccA=s96-c","user_score":1498,"rank":19},{"user_name":"Luis Enrique Pulido","user_username":"nosmirck","user_image_url":"https://graph.facebook.com/10212796907317782/picture?type=square&height=300&width=300","user_score":1492,"rank":20},{"user_name":"Alvin Sartor Go","user_username":"osweg0","user_image_url":"https://dcoder.tech/avatar/dev3.png","user_score":1487,"rank":21},{"user_name":"Noverdi A. Ramadhan","user_username":"noverdy","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GjQOdeHXD7mQtKqMKl_t8su7cTCMimE3ThXyVOaiA=s96-c","user_score":1464,"rank":22},{"user_name":"William Gray","user_username":"wagyourtail","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Gil4g-jvhQi2V-YkpSjRV59w7ibJ8AWp3ntTs04cg=s96-c","user_score":1464,"rank":22},{"user_name":"Adam Walker","user_username":"incursion75","user_image_url":"https://graph.facebook.com/10221089746814906/picture?type=square&height=300&width=300","user_score":1460,"rank":24},{"user_name":"Stanley Ibe","user_username":"ugoostanleyibe","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GiI_qWyTY7giDVmBuI1SF_SCc8_Lk4ioZmh8LzavA=s96-c","user_score":1457,"rank":25},{"user_name":"Anurag Negi","user_username":"anuragnegi","user_image_url":"https://lh3.googleusercontent.com/-1n9EhPSQe4g/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclbnHXJM0X5pAWRX2roRDnrjAImuA/s96-c/photo.jpg","user_score":1452,"rank":26},{"user_name":"Alvin Sartor C#","user_username":"oswego","user_image_url":"https://dcoder.tech/avatar/dev3.png","user_score":1444,"rank":27},{"user_name":"hamed zougouri","user_username":"demahrix","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GiZzWhbQf8eA34MMss3mgi9hKqYf5ifuiqR1Rg1TA=s96-c","user_score":1431,"rank":28},{"user_name":"SiVa KuMaR","user_username":"zen_of_python","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GiYIaH6c10qNqeDVyLHeblb1rzfBgxQ2yDNa6BDjA=s96-c","user_score":1414,"rank":29},{"user_name":"Jonas Alves","user_username":"gauss","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GguXWydZO-5TMM_jq3ePaGcygVrLSa35leBBfY=s96-c","user_score":1411,"rank":30},{"user_name":"Milos Zivic","user_username":"miloszivic99","user_image_url":"https://lh6.googleusercontent.com/-UFYNDEdUWGM/AAAAAAAAAAI/AAAAAAAACpo/AMZuucna0MbmJ9cnLEArpkElDbbIAOZokw/s96-c/photo.jpg","user_score":1406,"rank":31},{"user_name":"JaredCastro","user_username":"frigolombardi","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GiuNyAOHVNZuWzXvAnrgjT5C4mSS6_rRpZKV3y0gA=s96-c","user_score":1399,"rank":32},{"user_name":"Dmitriy Novak","user_username":"novak.knutd","user_image_url":"https://lh3.googleusercontent.com/-jYX_ZEAgMBA/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucm9vkR0WW2QLS8BVyrGl1iye_bzDg/s96-c/photo.jpg","user_score":1393,"rank":33},{"user_name":"Harjot Singh","user_username":"b18055","user_image_url":"https://lh3.googleusercontent.com/-DfthqsLx36o/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucnJd-0BBvcyy06gePZt-09chsCdWA/s96-c/photo.jpg","user_score":1383,"rank":34},{"user_name":"zxybar","user_username":"zxybar1","user_score":1379,"rank":35},{"user_name":"Miguel","user_username":"tsunglida","user_score":1374,"rank":36},{"user_name":"raj kumar lath","user_username":"raj.lath","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GhhEDyQHJpjyY4nqCW_z-_7MjmIgebhaI-LFmJ1Tg=s96-c","user_score":1370,"rank":37},{"user_name":"Landa Mohan","user_username":"landamohan","user_image_url":"https://dcoder.tech/avatar/dev3.png","user_score":1367,"rank":38},{"user_name":"Guillaume C.","user_username":"guillaume.curtil01","user_image_url":"https://lh5.googleusercontent.com/-I5tziVOlO8c/AAAAAAAAAAI/AAAAAAAAAGA/JcwFT3JH6f4/s96-c/photo.jpg","user_score":1366,"rank":39},{"user_name":"Hari Kumar","user_username":"harikumar","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GiA69SYifC0P_JXTnU5Jd4VYP_ZM_eUelldxLUaNg=s96-c","user_score":1360,"rank":40},{"user_name":"EXCEPTION","user_username":"maximumvalue","user_image_url":"https://dcoder.tech/avatar/dev2.png","user_score":1328,"rank":41},{"user_name":"luca5","user_username":"luca5","user_score":1323,"rank":42},{"user_name":"orenjiman","user_username":"orenjiman","user_score":1321,"rank":43},{"user_name":"Ahmed","user_username":"asadboghdadi","user_image_url":"https://lh5.googleusercontent.com/-U_8LQRxk8-E/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rewlHz4FfsOFhzJB3B4HklnoyQbxg/s96-c/photo.jpg","user_score":1321,"rank":43},{"user_name":"Manuel Prochnow","user_username":"kiuziu","user_score":1305,"rank":45},{"user_name":"praveen nani","user_username":"praveenvarikuppala","user_image_url":"https://graph.facebook.com/2395044587425924/picture?type=square&height=300&width=300","user_score":1305,"rank":45},{"user_name":"sergey","user_username":"sergey4spam","user_score":1298,"rank":47},{"user_name":"Jimmymonster","user_username":"twosoul1212312121","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Gi4BjNNcg4Wi7i6y_3_CYa2K-GNK4Dhl5Bt37MQXA=s96-c","user_score":1298,"rank":47},{"user_name":"Tauqeer Alam","user_username":"tauqeeralam289","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Gjsk_GZUvJ_wzJbE9FlKI6N5am69lth347I1Hha=s96-c","user_score":1298,"rank":47},{"user_name":"Andrea Barzaghi","user_username":"dbrn","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GgZFfeoS21XPIXQKScK1-Dl9efUlTSn1M6_Rwkv=s96-c","user_score":1297,"rank":50}],"profile":{"data":{"user_languages":[],"user_score":0,"user_name":"Gali pallavi","user_username":"anugali","stars":0,"forks":0,"codesin":[{"language_id":4,"percent":"100.00"}],"public_files":[],"submissions":null,"algo_progress":{"easySolved":0,"mediumSolved":0,"hardSolved":0,"easyTotal":84,"mediumTotal":72,"hardTotal":41}},"publicFiles":"","submissions":""},"isLoading":false},"common":{"isLogin":true,"dialogState":null,"theme":{"name":"dark","data":{"navbarBackground":"#050505","editorBackground":"#111111","outputBackgroundColor":"#282923","editorNavbar":"#454642","tabBackground":"#303030","textColor":"#bdbdbd","secondaryTextColor":"#424242","navbarIconColor":"#ffffff","adBackgroundColor":"#303030","editorBottomLineColor":"#272822"}},"publicProfile":{"data":{"followers":{"number":0,"followdata":[]},"user_languages":[],"user_score":22,"unsubmail":false,"user_name":"Shayaan Khan","user_email":"shayaankhan054@gmail.com","user_username":"shayaan7","user_image_url":"https://lh5.googleusercontent.com/-1nb1NF5pl-M/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucnmpU1lIQRoGocqLxkijgJfe3fDVg/s96-c/photo.jpg","profile_progress":"50%","stars":0,"forks":0,"codesin":[],"public_files":[],"submissions":[{"_id":"5f4cfd199d278545682c2cf5","score":5,"max_marks":5,"question_id":{"title":"Project Teams","level":"easy","_id":"5cf3f4881681076686eade89"}},{"_id":"5f4cc98e52a44f4562af3c0f","score":6,"max_marks":6,"question_id":{"title":"Leap Year","level":"easy","_id":"5b28ea8562db8b46ab2ac711"}},{"_id":"5f4cc7fc9d278545682bff7c","score":3,"max_marks":3,"question_id":{"title":"String Matching","level":"easy","_id":"5b211869ac71d7305eae7965"}}],"algo_progress":{"easySolved":5,"mediumSolved":0,"hardSolved":0,"easyTotal":84,"mediumTotal":72,"hardTotal":41}},"rank":"","countryRank":"","isPremium":false,"isLogin":true}},"feed":{"activeFile":{"_id":"5f458577b64dd92694afd9e8","user_id":{"_id":"5efa484eca5b3c6a2ad98c04","user_name":"uday More","user_username":"udaymore","user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Gg8i03fPPiYY8ygdI_1HLtZjW4OD26sB8hgVs6K1w=s96-c","id":"5efa484eca5b3c6a2ad98c04"},"generated_from":{},"is_template":false,"size":2449,"stars":{"number":138},"forks":{"number":44},"title":"Do you want to know how many seconds old you are ? ","description":"its very easy and simple code. I've made this code in a way that even beginner also can understand .\nyou will learn many more things just have a try \n","tags":["beginner"],"file":"age_.py","language_id":24,"updatedAt":"2020-08-30T10:04:13.172Z","createdAt":"2020-08-25T21:41:11.515Z","data":"","is_public":true,"is_linkshare_enabled":false,"is_readmode_default":true,"comments":{"number":29}},"feed":{"data":[{"type":1,"codes":[{"_id":"5f4693f97c3474269b006ba9","is_project":false,"size":3179,"user_id":{"user_image_url":"https://dcoder.tech/avatar/dev3.png","user_username":"ramaneffect","_id":"5f43fe7a2c9cf008df2c3c44"},"language_id":24,"file":"Enter Name and See Magic.py","public_file":"Enter Name and See Magic.py","title":"Type Name and See magic","description":"Name magic","tags":["tool","funny","tools","funny"],"createdAt":"2020-08-26T16:55:21.054Z","updatedAt":"2020-08-28T12:02:25.963Z","stars":{"number":213},"forks":{"number":80},"is_public":true,"has_errors":false,"output":{"data_type":1,"data":"Enter your name: \n\n1\n______________________________________\nIf you like it please give me a star.\n______________________________________\n"}},{"_id":"5f458577b64dd92694afd9e8","is_project":false,"size":2449,"user_id":{"user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Gg8i03fPPiYY8ygdI_1HLtZjW4OD26sB8hgVs6K1w=s96-c","user_username":"udaymore","_id":"5efa484eca5b3c6a2ad98c04"},"language_id":24,"file":"age_.py","public_file":"age_.py","title":"Do you want to know how many seconds old you are ? ","description":"its very easy and simple code. I've made this code in a way that even beginner also can understand .\nyou will learn many more things just have a try \n","tags":["beginner"],"createdAt":"2020-08-25T21:41:11.515Z","updatedAt":"2020-08-30T10:04:13.172Z","stars":{"number":138},"forks":{"number":44},"is_public":true,"has_errors":false,"output":{"data_type":1,"data":"__________________________________\n| What Is Your Name. ?            |\n|_________________________________|\nuday\n ___________________________________                                    \n|  Wow Thats V"}},{"_id":"5f47832f8ab0f5269c744ac8","is_project":false,"size":24057,"user_id":{"user_image_url":"https://dcoder.tech/avatar/dev3.png","user_username":"ramaneffect","_id":"5f43fe7a2c9cf008df2c3c44"},"language_id":400,"file":"WhatsApp Clone.html","public_file":"WhatsApp Clone.html","title":"WhatsApp Clone📧","description":"WhatsApp clone🤣🤣 give me star","tags":["WhatsApp"],"createdAt":"2020-08-27T09:55:59.829Z","updatedAt":"2020-08-27T10:39:30.136Z","stars":{"number":60},"forks":{"number":40},"is_public":true,"has_errors":false}],"challenges":null},{"type":2,"codes":[{"_id":"5f44b696718c7e1e0718670d","is_project":false,"size":4259,"user_id":{"user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GgAyuomxg2IdF8ug-qKQ03pN8SYHeRhTWHnpvtn=s96-c","user_username":"mickoutproject","_id":"5f0c17685b84c73f4857f0ae"},"language_id":400,"file":"P2.html","public_file":"P2.html","title":"CHOOSE YOUR FAVOURITE PROGRAMMING LANGUAGE HERE!!","description":"Choose your programming language","tags":["ILoveCoding"],"createdAt":"2020-08-25T06:58:30.571Z","updatedAt":"2020-08-27T16:51:36.480Z","stars":{"number":110},"forks":{"number":35},"is_public":true,"has_errors":false},{"_id":"5f3f6a6f8644863c4c982aa3","is_project":false,"size":13653,"user_id":{"user_image_url":"https://lh3.googleusercontent.com/a-/AOh14Gjb60qDpSc7tJGkUnwOnQtHbB53tydGiQ-DCea3=s96-c","user_username":"sharmapriyanshu938","_id":"5f2a61c9b5c86f4e11c80037"},"language_id":400,"file":"Golgi.html","public_file":"Golgi.html","title":"hardest game ever","description":"Hii if you win I follow you ","tags":["hardgame","hardestgame","game","html"],"createdAt":"2020-08-21T06:32:15.020Z","updatedAt":"2020-08-28T05:45:48.773Z","stars":{"number":236},"forks":{"number":123},"is_public":true,"has_errors":false},{"_id":"5f45b2f4b64dd92694afe3c6","is_project":false,"size":7832,"user_id":{"user_image_url":"https://dcoder.tech/avatar/dev1.png","user_username":"0ther","_id":"5f4462112c9cf008df2c5ad5"},"language_id":24,"file":"Hack.py","public_file":"Hack.py","title":"Most Advanced Computer Hack.","description":"Make sure to check out the other things I made on my profile! Greatly appreciated.","tags":["hacking","hack","python","python3"],"createdAt":"2020-08-26T00:55:16.383Z","updatedAt":"2020-08-28T18:36:27.221Z","stars":{"number":60},"forks":{"number":51},"is_public":true,"has_errors":false,"output":{"data_type":1,"data":"--------------------\nDownloading Free Ram\n--------------------\nHacking into your computer...\n=======================\nHacking proccess... 10%\nHacking proccess... 15%\nHacking proccess... 28%\nHacking pr"}}],"challenges":null},{"type":4,"codes":null,"challenges":[{"_id":"5de294592fcfb665c5f6596d","problem_setter":{"id":"5de25e832fcfb665c5f6593e","name":"Saurav Chandra"},"level":"hard","title":"Magic ChessBoard","question":"John has a magical chessboard. It looks like a normal chessboard except its size is N. Therefore the number of cells in the chessboard is N * N. He is interested in counting the number of squares in the chessboard. It is a very tough task for him, so he is looking for your help.","input":"First Line of the input contains an integer T denoting the number of test cases. The next T lines contain N, the size of the magic chessboard for each case.","output":"Print the number of squares in the chessboard.\n","constraints":"1 <= T <= 100\n1 <= N <= 100","sample_input":"3\n1\n2\n3","sample_output":"1\n5\n14","max_marks":16,"approved_at":"2020-06-15T14:49:42.286Z","solved_by":271},{"_id":"5e08a9dda1312802b296d21a","problem_setter":{"id":"5de25e832fcfb665c5f6593e","name":"Saurav Chandra"},"level":"medium","title":"Simple multiple problem","question":"You are given 2 numbers N and M. You have to find the smallest number which when multiplied to N makes it a multiple of M.\n","input":"First line contains T, number of test cases.\nEach of the next T lines contains two numbers, N and M.","output":"For each test case, print the required answer.","constraints":"1 <= T <= 100\n1 <= N, M <= 10^6","sample_input":"2\n4 7\n18 6\n","sample_output":"7\n1\n","max_marks":12,"approved_at":"2020-06-15T14:16:39.983Z","solved_by":388},{"_id":"5e1086efa1312802b296d39f","problem_setter":{"id":"5de25e832fcfb665c5f6593e","name":"Saurav Chandra"},"level":"easy","title":"Floating Number","question":"Bob has a floating point number N. He wants to set the precision for 2 digits after the decimal point for the number.\nHe is not good at coding, hence looking for your help.","input":"The first line contains T, the number of test cases.\nNext T line contains floating point number N.","output":"Print N in a separate line after setting precision for 2 digits after the decimal point:\n","constraints":"1 <= T <= 1000\n1 <= N <= 10000","sample_input":"1\n713.166\n","sample_output":"713.17\n","max_marks":4,"approved_at":"2020-06-15T14:13:32.171Z","solved_by":1240},{"_id":"5b28c8b162db8b46ab2ac69c","problem_setter":{"id":"5b18fcf7be95b1e1644787c0","name":"Bhanu Nadar"},"level":"hard","title":"Love For Mathematics","question":"Students of Dcoder school love Mathematics. They love to read a variety of Mathematics books. To make sure they remain happy,their Mathematics teacher decided to get more books for them.\nA student would become happy if there are at least X Mathematics books in the class and not more than Y books because they know \"All work and no play makes Jack a dull boy\".The teacher wants to buy a minimum number of books to make the maximum number of students happy.","input":"The first line of input contains an integer N indicating the number of students in the class. This is followed up by N lines where every line contains two integers X and Y respectively.","output":"Output two space-separated integers that denote the minimum number of mathematics books required and the maximum number of happy students.\nExplanation: \nThe teacher could buy 5 books and keep student 1, 2, 4 and 5 happy.","constraints":"1<=N<=10000\n1<=X,Y<=10^9","sample_input":"5\n3 6\n1 6\n7 11\n2 15\n5 8","sample_output":"5 4","max_marks":15,"approved_at":"2019-12-28T17:44:44.356Z","solved_by":353}]},{"type":3,"codes":[{"_id":"5f38f9dbdc55fe0e211b1aab","is_project":false,"size":635,"user_id":{"user_image_url":"https://lh3.googleusercontent.com/a-/AOh14GjKv8UQZuXax7gHJMo1pDivbGNsv2KyRy_0a2vpUg=s96-c","user_username":"arnab15y","_id":"5f1f86d65146e429a4666ae4"},"language_id":400,"file":"color.html","public_file":"color.html","title":"Magic Color","description":"You can change colour by typing name of any colour. Please try this one time.","tags":["magiccolor","magic","color","new","cool","trending"],"createdAt":"2020-08-16T09:18:19.693Z","updatedAt":"2020-08-25T08:15:38.438Z","stars":{"number":78},"forks":{"number":50},"is_public":true,"has_errors":false}],"challenges":null},{"type":3,"codes":[{"_id":"5f4a14e134fee545618b49af","is_project":false,"size":9169,"user_id":{"user_image_url":"https://dcoder.tech/avatar/dev3.png","user_username":"maskenilesh","_id":"5f2271a756557929ab91738d"},"language_id":4,"file":"Nilesh.java","public_file":"Nilesh.java","title":"I love you","description":"Java","tags":["#proposal"],"createdAt":"2020-08-29T08:42:09.246Z","updatedAt":"2020-08-30T15:14:51.111Z","stars":{"number":10},"forks":{"number":6},"is_public":true,"has_errors":false,"output":{"data_type":1,"data":":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n:::::::' .:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n::::'  .:::::::::::::::::::::::::::::::::::"}}],"challenges":null}],"pages":3,"isLoading":false,"searchData":"","searchPages":""},"mode":4},"myFiles":{"files":{"list":null,"count":null,"isLoading":false,"searchData":null,"searchPages":null},"mode":"","activeFile":""},"notification":{"isOpen":false,"message":""},"terminalLayout":1,"showTerminal":false,"reqURL":"http://code.dcoder.tech/question/5b85bc2bb6415039901fa9d4?lang=python3"}
          </script>
          <script>
            if ('serviceWorker' in navigator) {
              window.addEventListener('load', function() {
                navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
                  // Registration was successful
                  console.log('ServiceWorker registration successful with scope: ', registration.scope);
                }, function(err) {
                  // registration failed :(
                  console.log('ServiceWorker registration failed: ', err);
                }).catch(function(err) {
                  console.log(err)
                });
              });
            } else {
              console.log('service worker is not supported');
            }
          </script>
          <script src="./Happy String_files/jquery-3.3.1.min.js.download"></script>
      
  <div role="presentation" class="MuiDrawer-root MuiDrawer-modal" aria-hidden="true" style="position: fixed; z-index: 1300; right: 0px; bottom: 0px; top: 0px; left: 0px; visibility: hidden;"><div class="MuiBackdrop-root" aria-hidden="true" style="opacity: 0; visibility: hidden;"></div><div tabindex="0" data-test="sentinelStart"></div><div class="MuiPaper-root MuiDrawer-paper jss6 MuiDrawer-paperAnchorLeft MuiPaper-elevation16" tabindex="-1" style="visibility: hidden; transform: translateX(-70px);"><div id="sideBar" class="sidebar"><div class="jss5"><div style="height: 45px; box-sizing: border-box; padding: 10px; text-align: center;"><a href="https://code.dcoder.tech/" style="display: inline-block;"><div class="logoIcon"><img src="./Happy String_files/logo_dcoder.93662c17.png" style="height: 100%; width: 100%; padding: 4.5px; box-sizing: border-box;"></div></a></div></div><ul class="MuiList-root MuiList-padding"><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding: 0px;"><a title="Feed" href="https://code.dcoder.tech/feed" style="color: lightgray; text-decoration: none; width: 100%;"><div class="barIcon"><span class="icon icon-feed"></span><div style="text-align: center; font-size: 8px;">Feed</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding: 0px;"><a title="My Files" href="https://code.dcoder.tech/files" style="color: lightgray; text-decoration: none; width: 100%;"><div class="barIcon"><span class="icon icon-file"></span><div style="text-align: center; font-size: 8px;">My Files</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding: 0px;"><a title="Challenges" href="https://code.dcoder.tech/challenges" style="color: lightgray; text-decoration: none; width: 100%;"><div class="barIcon"><i class="icon icon-challenge"></i><div style="text-align: center; font-size: 8px;">Challenges</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding: 0px;"><a title="Leaderboard" href="https://code.dcoder.tech/leaderboard" style="color: lightgray; text-decoration: none; width: 100%;"><div class="barIcon"><span class="icon icon-leaderboard"></span><div style="text-align: center; font-size: 8px;">Leaderboard</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding: 0px;"><a title="Dev Chat" href="https://code.dcoder.tech/devchat" style="color: lightgray; text-decoration: none; width: 100%;"><div class="barIcon"><i class="icon icon-devchat"></i><div style="text-align: center; font-size: 8px;">Dev Chat</div></div></a><span class="MuiTouchRipple-root"></span></div><div class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button" tabindex="0" role="button" aria-disabled="false" style="padding: 0px;"><a title="Settings" href="https://code.dcoder.tech/settings/profile" style="color: lightgray; text-decoration: none; width: 100%;"><div class="barIcon"><i class="icon icon-setting"></i><div style="text-align: center; font-size: 8px;">Settings</div></div></a><span class="MuiTouchRipple-root"></span></div></ul><a href="https://code.dcoder.tech/profile/shayaan7" style="color: lightgray; text-decoration: none; width: 100%;"><div class="barIcon last" style="position: absolute; bottom: 10px;"><img src="./Happy String_files/photo.jpg" alt="profile pic" style="height: 30px; width: 30px; border-radius: 50%;"><div style="text-align: center; font-size: 10px; overflow: hidden; text-overflow: ellipsis; padding: 0px 5px;">@shayaan7</div></div></a></div></div><div tabindex="0" data-test="sentinelEnd"></div></div></body></html>