export const EMPTY = '' as const;

export type Empty = typeof EMPTY;

/**
 * スタイル
 */
export const STYLE = {
  // 基本色
  BASE_COLOR: '#1f1f1f',
  // 基本背景色
  BASE_BACKGROUND_COLOR: '#c7e1ff',
  // メニュー背景色
  MENU_BACKGROUND_COLOR: '#ebafb5',
  // ヘッダー背景色
  HEAD_BACKGROUND_COLOR: '#c5e5ff',
  // 基本フォントサイズ
  BASE_FONT_SIZE: 12,
  // 基本項目高さ
  BASE_ITEM_HEIGHT: 24,
} as const;
