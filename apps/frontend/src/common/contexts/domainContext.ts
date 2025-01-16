import { createContext, useContext } from 'react';

const DomainContext = createContext(null);

export const DomainProvider = DomainContext.Provider;
export const useDomain = () => useContext(DomainContext);
