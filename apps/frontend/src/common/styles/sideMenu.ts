import { Link } from 'react-router-dom';

import { ListItemButton } from '@mui/material';
import { styled } from '@mui/material/styles';

import { STYLE } from '@/common/config/consts';

/**
 * サイドメニューのリストアイテムスタイル
 */
export const ListItemStyle = styled('div')({
  borderBottom: '1px solid #d8d8d8',
});

/**
 * サイドメニューのリストアイテムボタンスタイル
 */
export const ListItemButtonStyle = styled(ListItemButton)(() => ({
  paddingTop: 15,
  paddingBottom: 15,
}));

/**
 * サイドメニューのサブリストアイテムボタンスタイル
 */
export const SubListItemButtonStyle = styled(ListItemButton)(() => ({
  paddingLeft: 40,
  '&.Mui-selected': {
    background: '#98cfff',
  },
}));

/**
 * リンクスタイル
 */
export const LinkStyle = styled(Link)(() => ({
  color: STYLE.BASE_COLOR,
  textDecoration: 'none',
}));
