/**
 * パンくずリスト モジュールコンポーネント
 */
import { JSX, useMemo } from 'react';

import MenuIcon from '@mui/icons-material/Menu';
import { AppBar, Toolbar, IconButton, Box, Typography } from '@mui/material';

import { useSelectedPage } from '@/shared/contexts/pageContext';

export type BreadcrumbProps = {
  sideMenuOpen: boolean;
  setSideMenuOpen: React.Dispatch<React.SetStateAction<boolean>>;
};

/**
 * パンくずリスト
 * @param sideMenuOpen サイドメニュー開閉フラグ
 * @param setSideMenuOpen サイドメニュー開閉フラグ設定関数
 * @returns {JSX.Element} JSX.Element
 */
const Breadcrumb = ({ sideMenuOpen, setSideMenuOpen }: BreadcrumbProps): JSX.Element => {
  const selectedPage = useSelectedPage();

  const categoryMemo = useMemo(() => {
    if (selectedPage.categoryName) {
      return (
        <>
          <Box component="span">{selectedPage.categoryName.toString()}</Box>
          <Box component="span" sx={{ ml: 1, mr: 1 }}>
            ＞
          </Box>
        </>
      );
    }
    return '';
  }, [selectedPage]);

  return (
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
        {categoryMemo}
        <Typography component="h1" sx={{ fontSize: 14, fontWeight: 'bold' }}>
          {selectedPage.pageName?.toString()}
        </Typography>
      </Toolbar>
    </AppBar>
  );
};
export default Breadcrumb;
