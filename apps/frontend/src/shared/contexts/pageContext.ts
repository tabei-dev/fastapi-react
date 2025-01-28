import { useEffect } from 'react';

import { atom, useSetAtom, useAtomValue } from 'jotai';

const selectedPageState = atom({ categoryName: '', pageName: '' } as {
  categoryName: string;
  pageName: string;
});

export const useSetSelectedPage = ({
  categoryName,
  pageName,
}: {
  categoryName: string;
  pageName: string;
}) => {
  const setSelectedPage = useSetAtom(selectedPageState);

  useEffect(() => {
    setSelectedPage({
      categoryName,
      pageName,
    });
  }, [categoryName, pageName, setSelectedPage]);
};

export const useSelectedPage = () => useAtomValue(selectedPageState);
