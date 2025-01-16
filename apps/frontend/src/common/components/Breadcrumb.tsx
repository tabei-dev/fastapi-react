/**
 * パンくずリスト モジュールコンポーネント
 */
import { JSX } from 'react';

import MenuIcon from '@mui/icons-material/Menu';
import { AppBar, Toolbar, IconButton, Box, Typography } from '@mui/material';

// import { ICategoryType, IPageType } from '@/common/config/types';

export type BreadcrumbProps = {
  category: string | undefined;
  page: string | undefined;
  sideMenuOpen: boolean;
  setSideMenuOpen: React.Dispatch<React.SetStateAction<boolean>>;
};

/**
 * パンくずリスト
 * @param category カテゴリ
 * @param page ページ
 * @param sideMenuOpen サイドメニュー開閉フラグ
 * @param setSideMenuOpen サイドメニュー開閉フラグ設定関数
 * @returns {JSX.Element} JSX.Element
 */
const Breadcrumb = ({
  category,
  page,
  sideMenuOpen,
  setSideMenuOpen,
}: BreadcrumbProps): JSX.Element => (
  <AppBar position="static" color="inherit">
    <Toolbar variant="dense">
      <IconButton
        edge="start"
        sx={{
          mr: 2,
          // サイドメニューが表示されているときはメニューアイコンは表示しない
          ...(sideMenuOpen && { display: 'none' }),
        }}
        onClick={() => setSideMenuOpen(true)}
      >
        <MenuIcon />
      </IconButton>
      {category && (
        <>
          <Box component="span">{category.toString()}</Box>
          <Box component="span" sx={{ ml: 1, mr: 1 }}>
            ＞
          </Box>
        </>
      )}
      <Typography component="h1" sx={{ fontSize: 14, fontWeight: 'bold' }}>
        {page?.toString()}
      </Typography>
    </Toolbar>
  </AppBar>
);
export default Breadcrumb;
